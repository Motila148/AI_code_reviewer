from __future__ import annotations

import io
import tokenize
from typing import Any


MAX_LINE_LENGTH = 88


def review_style(code: str) -> list[dict[str, Any]]:
    """Run lightweight PEP-oriented checks without third-party linters."""
    findings: list[dict[str, Any]] = []
    seen_keys: set[tuple[str, int, str]] = set()
    lines = code.splitlines()

    def add_finding(rule: str, message: str, line: int, severity: str = "info") -> None:
        key = (rule, line, message)
        if key in seen_keys:
            return

        seen_keys.add(key)
        findings.append(
            {
                "category": "Style",
                "severity": severity,
                "rule": rule,
                "line": line,
                "message": message,
            }
        )

    for line_number, line in enumerate(lines, start=1):
        if "\t" in line:
            add_finding(
                "tabs",
                "Replace tab characters with spaces to keep indentation consistent.",
                line_number,
                "warning",
            )

        if line.rstrip(" ") != line:
            add_finding(
                "trailing-whitespace",
                "Trailing whitespace makes diffs noisy and should be removed.",
                line_number,
            )

        if len(line) > MAX_LINE_LENGTH:
            add_finding(
                "line-length",
                f"Line length is {len(line)} characters; consider wrapping lines beyond {MAX_LINE_LENGTH}.",
                line_number,
            )

        stripped = line.strip()
        if ";" in line and stripped and not stripped.startswith("#"):
            add_finding(
                "multiple-statements",
                "Avoid placing multiple statements on one line.",
                line_number,
            )

    if code and not code.endswith("\n"):
        add_finding(
            "missing-eof-newline",
            "PEP-friendly files usually end with a newline.",
            len(lines),
        )

    blank_run = 0
    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped:
            blank_run += 1
            continue

        if stripped.startswith(("def ", "class ")) and line == line.lstrip(" "):
            if blank_run > 2:
                add_finding(
                    "blank-lines",
                    "Top-level definitions should usually be separated by two blank lines, not more.",
                    line_number,
                )
        blank_run = 0

    try:
        tokens = tokenize.generate_tokens(io.StringIO(code).readline)
        for token_type, token_string, start, _, _ in tokens:
            if token_type != tokenize.INDENT:
                continue

            if "\t" in token_string:
                add_finding(
                    "indentation-tabs",
                    "Indentation should use spaces rather than tabs.",
                    start[0],
                    "warning",
                )

            visual_width = len(token_string.replace("\t", "    "))
            if visual_width % 4 != 0:
                add_finding(
                    "indentation-width",
                    "Block indentation should usually be a multiple of four spaces.",
                    start[0],
                    "warning",
                )
    except tokenize.TokenError:
        pass

    return sorted(findings, key=lambda item: (item["line"], item["message"]))
