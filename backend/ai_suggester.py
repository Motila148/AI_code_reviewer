from __future__ import annotations

import os
import re
from typing import Any

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - optional during minimal local verification
    def load_dotenv() -> bool:
        return False


def _format_static_findings(findings: list[dict[str, Any]]) -> str:
    if not findings:
        return "- No static analysis findings were detected."

    lines: list[str] = []
    for finding in findings[:12]:
        location = f"line {finding['line']}" if finding.get("line") else "general"
        lines.append(
            f"- [{finding['severity'].upper()}] {finding['category']} at {location}: "
            f"{finding['message']}"
        )
    return "\n".join(lines)


def _parse_tagged_response(content: str, original_code: str) -> dict[str, str]:
    analysis_match = re.search(r"<analysis>\s*(.*?)\s*</analysis>", content, re.DOTALL)
    corrected_match = re.search(
        r"<corrected_code>\s*```python\s*(.*?)\s*```\s*</corrected_code>",
        content,
        re.DOTALL,
    )

    analysis = (
        analysis_match.group(1).strip()
        if analysis_match
        else content.strip()
    )
    corrected_code = (
        corrected_match.group(1).strip()
        if corrected_match
        else ""
    )

    if not corrected_code:
        corrected_code = original_code.strip()

    return {
        "analysis": analysis,
        "corrected_code": corrected_code,
    }


def _groq_review(code: str, static_findings: list[dict[str, Any]], api_key: str) -> dict[str, str]:
    try:
        from langchain_groq import ChatGroq
        from langchain_core.prompts import PromptTemplate
    except ImportError:
        return {
            "status": "unavailable",
            "provider": "groq",
            "analysis": (
                "Install the LangChain Groq integration to enable model-backed reviews. "
                "Static analysis results are still available."
            ),
            "corrected_code": code.strip(),
        }

    prompt_template = PromptTemplate(
        input_variables=["code_string", "static_findings"],
        template="""
You are an experienced coding teacher and Python reviewer.

Use the static findings and the code below to produce a careful review.
Return the result using exactly this format:
<analysis>
- Correctness Risks
- Logic or Edge Cases
- PEP 8 / Readability Notes
- Performance Notes
- Recommended Next Steps

Explain why each suggestion matters for the student.
</analysis>
<corrected_code>
```python
# Put the corrected and improved Python code here.
```
</corrected_code>

Static findings:
{static_findings}

Code:
{code_string}
""".strip(),
    )
    model_name = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")

    try:
        model = ChatGroq(model_name=model_name, api_key=api_key, temperature=0)
        formatted_prompt = prompt_template.format(
            code_string=code,
            static_findings=_format_static_findings(static_findings),
        )
        result = model.invoke(formatted_prompt)
        content = getattr(result, "content", "").strip()
        if not content:
            content = "The LLM completed the call but returned an empty review."
        parsed = _parse_tagged_response(content, code)
        return {
            "status": "available",
            "provider": "groq",
            "analysis": parsed["analysis"],
            "corrected_code": parsed["corrected_code"],
        }
    except Exception as exc:  # pragma: no cover - depends on external network/API state
        return {
            "status": "error",
            "provider": "groq",
            "analysis": (
                "The Groq review could not be completed. "
                f"Groq returned: {exc}"
            ),
            "corrected_code": code.strip(),
        }


def get_ai_suggestion(code: str, static_findings: list[dict[str, Any]]) -> dict[str, str]:
    """Request an LLM review and corrected code using Groq, aligned with ChatGroq usage."""
    load_dotenv()

    groq_api_key = os.getenv("GROQ_API_KEY") or os.getenv("GROK_API_KEY")
    grok_alias_key = os.getenv("GROK_API_KEY")
    xai_api_key = os.getenv("XAI_API_KEY")

    if groq_api_key:
        return _groq_review(
            code=code,
            static_findings=static_findings,
            api_key=groq_api_key,
        )

    return {
        "status": "unavailable",
        "provider": "none",
        "analysis": (
            "No Groq key was detected for ChatGroq. Set GROQ_API_KEY."
            + (" GROK_API_KEY is also accepted as a compatibility alias." if grok_alias_key else "")
            + (
                " XAI_API_KEY is not used by the current Groq-only setup."
                if xai_api_key
                else ""
            )
        ),
        "corrected_code": code.strip(),
    }
