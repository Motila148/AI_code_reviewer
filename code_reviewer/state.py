from __future__ import annotations

import reflex as rx

from backend.analyzer import analyze_code_pipeline


SAMPLE_CODE = """import math


def compute_average(values=[]):
    total = 0
    for value in values:
        total += value
        return total / len(values)


def risky_division():
    number = 10 / 0
    print(number)
"""


def _format_issue(issue: dict) -> str:
    severity = str(issue.get("severity", "info")).upper()
    category = issue.get("category", "Issue")
    line = issue.get("line", 0)
    rule = issue.get("rule", "")
    location = f"Line {line}" if line else "General"
    rule_suffix = f" [{rule}]" if rule else ""
    return f"{severity} - {category} - {location}{rule_suffix}: {issue.get('message', '')}"


class CodeState(rx.State):
    code_input: str = ""
    uploaded_filename: str = ""
    syntax_message: str = "Upload a Python file or paste code to start the review."
    review_summary: str = ""
    findings: list[str] = []
    has_findings: bool = False
    llm_review: str = ""
    corrected_code: str = ""
    llm_status: str = "idle"
    llm_provider: str = "none"
    error_message: str = ""
    review_ready: bool = False
    syntax_ok: bool = False
    is_loading: bool = False
    line_count: int = 0
    non_empty_lines: int = 0
    function_count: int = 0
    class_count: int = 0
    import_count: int = 0
    error_count: int = 0
    warning_count: int = 0
    info_count: int = 0

    def update_code_input(self, value: str) -> None:
        self.code_input = value

    async def handle_upload(self, files: list[rx.UploadFile]) -> None:
        self.error_message = ""

        if not files:
            self.error_message = "Choose a Python file before trying to load it."
            return

        selected_file = files[0]
        filename = selected_file.filename or "uploaded_code.py"
        lower_name = filename.lower()

        if not lower_name.endswith((".py", ".pyi", ".txt")):
            self.error_message = "Only .py, .pyi, and .txt files are supported."
            return

        raw_bytes = await selected_file.read()
        try:
            decoded = raw_bytes.decode("utf-8")
        except UnicodeDecodeError:
            decoded = raw_bytes.decode("latin-1")

        self.code_input = decoded
        self.uploaded_filename = filename
        self.review_ready = False
        self.syntax_message = f"Loaded '{filename}'. Run the analysis when you are ready."

    async def analyze(self) -> None:
        if not self.code_input.strip():
            self.error_message = "Paste code or load a file before running the review."
            self.review_ready = False
            return

        self.error_message = ""
        self.is_loading = True
        yield

        report = analyze_code_pipeline(
            self.code_input,
            self.uploaded_filename or "pasted_snippet.py",
        )

        self.syntax_ok = report["syntax_ok"]
        self.syntax_message = report["syntax_message"]
        self.review_summary = report["summary"]
        self.findings = [_format_issue(issue) for issue in report["issues"]]
        self.has_findings = len(self.findings) > 0
        self.llm_review = report["llm_review"]["analysis"]
        self.corrected_code = report["llm_review"]["corrected_code"]
        self.llm_status = report["llm_review"]["status"]
        self.llm_provider = report["llm_review"].get("provider", "none")
        self.review_ready = True

        stats = report["stats"]
        self.line_count = int(stats.get("line_count", 0))
        self.non_empty_lines = int(stats.get("non_empty_lines", 0))
        self.function_count = int(stats.get("function_count", 0))
        self.class_count = int(stats.get("class_count", 0))
        self.import_count = int(stats.get("import_count", 0))

        counts = report["counts"]
        self.error_count = int(counts.get("error", 0))
        self.warning_count = int(counts.get("warning", 0))
        self.info_count = int(counts.get("info", 0))
        self.is_loading = False

    def load_sample(self) -> None:
        self.code_input = SAMPLE_CODE
        self.uploaded_filename = "sample_reviewer_input.py"
        self.syntax_message = "Sample code loaded. Run the analysis to see the pipeline in action."
        self.error_message = ""
        self.review_ready = False

    def clear_workspace(self) -> None:
        self.code_input = ""
        self.uploaded_filename = ""
        self.syntax_message = "Upload a Python file or paste code to start the review."
        self.review_summary = ""
        self.findings = []
        self.has_findings = False
        self.llm_review = ""
        self.corrected_code = ""
        self.llm_status = "idle"
        self.llm_provider = "none"
        self.error_message = ""
        self.review_ready = False
        self.syntax_ok = False
        self.is_loading = False
        self.line_count = 0
        self.non_empty_lines = 0
        self.function_count = 0
        self.class_count = 0
        self.import_count = 0
        self.error_count = 0
        self.warning_count = 0
        self.info_count = 0
