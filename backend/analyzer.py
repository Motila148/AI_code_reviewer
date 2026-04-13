from __future__ import annotations

from typing import Any

from backend.ai_suggester import get_ai_suggestion
from backend.ast_reviewer import ASTReviewer
from backend.code_parser import collect_code_stats, parse_code
from backend.style_reviewer import review_style


def _severity_counts(findings: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"error": 0, "warning": 0, "info": 0}
    for finding in findings:
        severity = finding.get("severity", "info")
        counts[severity] = counts.get(severity, 0) + 1
    return counts


def _build_summary(syntax_ok: bool, findings: list[dict[str, Any]]) -> str:
    if not syntax_ok:
        return "The file could not be parsed, so only syntax feedback is available."

    if not findings:
        return "No static issues were detected. The code is ready for the LLM pass."

    counts = _severity_counts(findings)
    return (
        f"Static review found {len(findings)} issue(s): "
        f"{counts['error']} error(s), {counts['warning']} warning(s), and {counts['info']} note(s)."
    )


def analyze_code_pipeline(code: str, filename: str = "snippet.py") -> dict[str, Any]:
    """Run syntax, style, AST heuristics, and optional LLM review."""
    syntax_result = parse_code(code)

    if not syntax_result["success"]:
        syntax_issue = syntax_result["error"]
        issue_list = [syntax_issue]
        return {
            "filename": filename,
            "syntax_ok": False,
            "syntax_message": syntax_issue["message"],
            "summary": _build_summary(False, issue_list),
            "issues": issue_list,
            "stats": {
                "line_count": len(code.splitlines()),
                "non_empty_lines": sum(1 for line in code.splitlines() if line.strip()),
                "function_count": 0,
                "class_count": 0,
                "import_count": 0,
            },
            "counts": _severity_counts(issue_list),
            "llm_review": {
                "status": "skipped",
                "provider": "none",
                "analysis": "Resolve syntax errors first, then rerun the review for LLM feedback.",
                "corrected_code": code.strip(),
            },
        }

    tree = syntax_result["tree"]
    style_findings = review_style(code)
    ast_findings = ASTReviewer().review(tree)
    findings = sorted(
        [*style_findings, *ast_findings],
        key=lambda item: (
            {"error": 0, "warning": 1, "info": 2}.get(item["severity"], 9),
            item.get("line", 0),
            item["message"],
        ),
    )
    llm_review = get_ai_suggestion(code, findings)
    return {
        "filename": filename,
        "syntax_ok": True,
        "syntax_message": "Python syntax parsed successfully.",
        "summary": _build_summary(True, findings),
        "issues": findings,
        "stats": collect_code_stats(code, tree),
        "counts": _severity_counts(findings),
        "llm_review": llm_review,
    }
