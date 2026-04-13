from __future__ import annotations

import ast
import builtins
from typing import Any


TERMINATOR_NODES = (ast.Return, ast.Raise, ast.Break, ast.Continue)


class ASTReviewer(ast.NodeVisitor):
    """Heuristic AST review for probable logic and maintainability issues."""

    def __init__(self) -> None:
        self.findings: list[dict[str, Any]] = []
        self._seen_keys: set[tuple[str, int, str]] = set()
        self._used_names: set[str] = set()
        self._assigned_names: dict[str, tuple[int, str]] = {}
        self._imported_names: dict[str, int] = {}
        self._function_stack: list[dict[str, Any]] = []
        self._builtin_names = set(dir(builtins))

    def review(self, tree: ast.AST) -> list[dict[str, Any]]:
        if isinstance(tree, ast.Module):
            self._check_block(tree.body, "module body")
        self.visit(tree)
        self._report_unused_names()
        return self._sorted_findings()

    def _sorted_findings(self) -> list[dict[str, Any]]:
        severity_order = {"error": 0, "warning": 1, "info": 2}
        return sorted(
            self.findings,
            key=lambda item: (
                severity_order.get(item["severity"], 9),
                item.get("line", 0),
                item["message"],
            ),
        )

    def _add_finding(
        self,
        *,
        category: str,
        severity: str,
        rule: str,
        message: str,
        line: int = 0,
    ) -> None:
        key = (rule, line, message)
        if key in self._seen_keys:
            return

        self._seen_keys.add(key)
        self.findings.append(
            {
                "category": category,
                "severity": severity,
                "rule": rule,
                "line": line,
                "message": message,
            }
        )

    def _check_block(self, statements: list[ast.stmt], block_name: str) -> None:
        for index, statement in enumerate(statements[:-1]):
            if isinstance(statement, TERMINATOR_NODES):
                next_statement = statements[index + 1]
                self._add_finding(
                    category="Logic",
                    severity="warning",
                    rule="unreachable-code",
                    line=getattr(next_statement, "lineno", 0),
                    message=f"Code after this statement in the {block_name} is unreachable.",
                )
                break

    def _report_unused_names(self) -> None:
        ignored_names = {"self", "cls"}

        for name, line in self._imported_names.items():
            if name.startswith("_") or name in self._used_names:
                continue
            self._add_finding(
                category="Maintainability",
                severity="warning",
                rule="unused-import",
                line=line,
                message=f"Imported name '{name}' is never used.",
            )

        for name, (line, kind) in self._assigned_names.items():
            if name.startswith("_") or name in ignored_names or name in self._used_names:
                continue
            self._add_finding(
                category="Maintainability",
                severity="info",
                rule=f"unused-{kind}",
                line=line,
                message=f"{kind.capitalize()} '{name}' is assigned but never read.",
            )

    def _register_assignment(self, name: str, line: int, kind: str = "variable") -> None:
        if name in {"self", "cls"}:
            return
        self._assigned_names.setdefault(name, (line, kind))

    def _extract_target_names(self, node: ast.AST) -> list[str]:
        names: list[str] = []
        if isinstance(node, ast.Name):
            names.append(node.id)
        elif isinstance(node, (ast.Tuple, ast.List)):
            for child in node.elts:
                names.extend(self._extract_target_names(child))
        return names

    def _check_shadowed_builtins(self, node: ast.AST, targets: list[str]) -> None:
        for target in targets:
            if target in self._builtin_names and target not in {"id", "type"}:
                self._add_finding(
                    category="Logic",
                    severity="warning",
                    rule="shadowed-builtin",
                    line=getattr(node, "lineno", 0),
                    message=(
                        f"Assignment to '{target}' shadows the Python builtin and can lead "
                        "to confusing runtime behavior."
                    ),
                )

    def _visit_function(self, node: ast.FunctionDef | ast.AsyncFunctionDef) -> None:
        arg_count = len(node.args.args) + len(node.args.kwonlyargs)
        if node.args.vararg:
            arg_count += 1
        if node.args.kwarg:
            arg_count += 1

        if arg_count > 6:
            self._add_finding(
                category="Maintainability",
                severity="info",
                rule="many-parameters",
                line=node.lineno,
                message=(
                    f"Function '{node.name}' accepts {arg_count} parameters; consider "
                    "simplifying the signature if the API feels hard to use."
                ),
            )

        if hasattr(node, "end_lineno"):
            length = node.end_lineno - node.lineno + 1
            if length > 50:
                self._add_finding(
                    category="Maintainability",
                    severity="info",
                    rule="long-function",
                    line=node.lineno,
                    message=(
                        f"Function '{node.name}' spans {length} lines; splitting it can "
                        "make reviews and testing easier."
                    ),
                )

        for default_value in [*node.args.defaults, *node.args.kw_defaults]:
            if isinstance(default_value, (ast.List, ast.Dict, ast.Set)):
                self._add_finding(
                    category="Logic",
                    severity="warning",
                    rule="mutable-default",
                    line=getattr(default_value, "lineno", node.lineno),
                    message=(
                        f"Function '{node.name}' uses a mutable default argument, which can "
                        "retain state between calls."
                    ),
                )

        for argument in [*node.args.args, *node.args.kwonlyargs]:
            self._register_assignment(
                argument.arg,
                getattr(argument, "lineno", node.lineno),
                "argument",
            )

        self._function_stack.append(
            {"name": node.name, "returns_value": False, "returns_empty": False}
        )
        self._check_block(node.body, f"function '{node.name}'")
        self.generic_visit(node)
        function_state = self._function_stack.pop()

        if function_state["returns_value"] and function_state["returns_empty"]:
            self._add_finding(
                category="Logic",
                severity="warning",
                rule="inconsistent-return",
                line=node.lineno,
                message=(
                    f"Function '{node.name}' mixes bare returns and value returns, which "
                    "can make callers harder to reason about."
                ),
            )

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._visit_function(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._visit_function(node)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            imported_name = alias.asname or alias.name.split(".")[0]
            self._imported_names.setdefault(imported_name, node.lineno)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for alias in node.names:
            imported_name = alias.asname or alias.name
            self._imported_names.setdefault(imported_name, node.lineno)
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        targets: list[str] = []
        for target in node.targets:
            extracted = self._extract_target_names(target)
            targets.extend(extracted)
            for name in extracted:
                self._register_assignment(name, node.lineno)

        self._check_shadowed_builtins(node, targets)
        self.generic_visit(node)

    def visit_AnnAssign(self, node: ast.AnnAssign) -> None:
        targets = self._extract_target_names(node.target)
        for name in targets:
            self._register_assignment(name, node.lineno)
        self._check_shadowed_builtins(node, targets)
        self.generic_visit(node)

    def visit_For(self, node: ast.For) -> None:
        for name in self._extract_target_names(node.target):
            self._register_assignment(name, node.lineno)
        self._check_block(node.body, "for loop")
        self._check_block(node.orelse, "for-else block")
        self.generic_visit(node)

    def visit_AsyncFor(self, node: ast.AsyncFor) -> None:
        for name in self._extract_target_names(node.target):
            self._register_assignment(name, node.lineno)
        self._check_block(node.body, "async for loop")
        self._check_block(node.orelse, "async for-else block")
        self.generic_visit(node)

    def visit_With(self, node: ast.With) -> None:
        for item in node.items:
            if item.optional_vars:
                for name in self._extract_target_names(item.optional_vars):
                    self._register_assignment(name, node.lineno)
        self._check_block(node.body, "with block")
        self.generic_visit(node)

    def visit_AsyncWith(self, node: ast.AsyncWith) -> None:
        for item in node.items:
            if item.optional_vars:
                for name in self._extract_target_names(item.optional_vars):
                    self._register_assignment(name, node.lineno)
        self._check_block(node.body, "async with block")
        self.generic_visit(node)

    def visit_Name(self, node: ast.Name) -> None:
        if isinstance(node.ctx, ast.Load):
            self._used_names.add(node.id)
        self.generic_visit(node)

    def visit_Return(self, node: ast.Return) -> None:
        if self._function_stack:
            if node.value is None:
                self._function_stack[-1]["returns_empty"] = True
            else:
                self._function_stack[-1]["returns_value"] = True
        self.generic_visit(node)

    def visit_If(self, node: ast.If) -> None:
        if isinstance(node.test, ast.Constant):
            self._add_finding(
                category="Logic",
                severity="warning",
                rule="constant-condition",
                line=node.lineno,
                message="This conditional uses a constant truth value and will always branch the same way.",
            )

        self._check_block(node.body, "if block")
        self._check_block(node.orelse, "else block")
        self.generic_visit(node)

    def visit_While(self, node: ast.While) -> None:
        if isinstance(node.test, ast.Constant) and node.test.value is True:
            has_break = any(isinstance(child, ast.Break) for child in ast.walk(node))
            if not has_break:
                self._add_finding(
                    category="Logic",
                    severity="warning",
                    rule="possible-infinite-loop",
                    line=node.lineno,
                    message="This 'while True' loop has no break statement and may never terminate.",
                )

        self._check_block(node.body, "while loop")
        self._check_block(node.orelse, "while-else block")
        self.generic_visit(node)

    def visit_Try(self, node: ast.Try) -> None:
        self._check_block(node.body, "try block")
        self._check_block(node.orelse, "try-else block")
        self._check_block(node.finalbody, "finally block")
        for handler in node.handlers:
            self._check_block(handler.body, "except block")
        self.generic_visit(node)

    def visit_ExceptHandler(self, node: ast.ExceptHandler) -> None:
        if node.type is None:
            self._add_finding(
                category="Logic",
                severity="warning",
                rule="bare-except",
                line=node.lineno,
                message="A bare except catches system-exiting exceptions and can hide real failures.",
            )
        elif isinstance(node.type, ast.Name) and node.type.id == "Exception":
            self._add_finding(
                category="Logic",
                severity="info",
                rule="broad-except",
                line=node.lineno,
                message="Catching generic Exception may hide useful failure details.",
            )
        self.generic_visit(node)

    def visit_Compare(self, node: ast.Compare) -> None:
        if any(
            isinstance(comparator, ast.Constant) and comparator.value is None
            for comparator in node.comparators
        ):
            if any(isinstance(operator, (ast.Eq, ast.NotEq)) for operator in node.ops):
                self._add_finding(
                    category="Style",
                    severity="info",
                    rule="none-comparison",
                    line=node.lineno,
                    message="Compare to None with 'is' or 'is not' instead of equality operators.",
                )
        self.generic_visit(node)

    def visit_BinOp(self, node: ast.BinOp) -> None:
        if isinstance(node.op, (ast.Div, ast.FloorDiv, ast.Mod)) and isinstance(
            node.right, ast.Constant
        ):
            if node.right.value == 0:
                self._add_finding(
                    category="Logic",
                    severity="error",
                    rule="division-by-zero",
                    line=node.lineno,
                    message="This expression divides by zero and will raise an exception at runtime.",
                )
        self.generic_visit(node)
