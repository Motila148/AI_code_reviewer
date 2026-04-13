from __future__ import annotations

import ast
from typing import Any


def parse_code(code_string: str) -> dict[str, Any]:
    """Parse Python source and return either the AST or a structured syntax error."""
    normalized = code_string.replace("\r\n", "\n")

    if not normalized.strip():
        return {
            "success": False,
            "error": {
                "category": "Syntax",
                "severity": "error",
                "rule": "empty-input",
                "line": 0,
                "message": "No Python code was provided for analysis.",
            },
        }

    try:
        tree = ast.parse(normalized)
    except SyntaxError as exc:
        message = exc.msg or "Invalid Python syntax."
        line = exc.lineno or 0
        column = exc.offset or 0
        snippet = (exc.text or "").strip()
        location = f"line {line}, column {column}" if line else "unknown location"

        return {
            "success": False,
            "error": {
                "category": "Syntax",
                "severity": "error",
                "rule": "python-parse",
                "line": line,
                "message": f"{message} at {location}.",
                "details": snippet,
            },
        }

    return {"success": True, "tree": tree}


def collect_code_stats(code_string: str, tree: ast.AST) -> dict[str, int]:
    """Return lightweight code stats for the review dashboard."""
    lines = code_string.splitlines()

    return {
        "line_count": len(lines),
        "non_empty_lines": sum(1 for line in lines if line.strip()),
        "function_count": sum(
            isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            for node in ast.walk(tree)
        ),
        "class_count": sum(isinstance(node, ast.ClassDef) for node in ast.walk(tree)),
        "import_count": sum(
            isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree)
        ),
    }
