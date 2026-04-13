import reflex as rx

from .components.navbar import navbar
from .state import CodeState


UPLOAD_ID = "python_code_upload"


def stat_card(label: str, value, accent: str) -> rx.Component:
    return rx.vstack(
        rx.box(
            width="0.72rem",
            height="0.72rem",
            border_radius="999px",
            background=accent,
        ),
        rx.text(
            label,
            font_size="0.78rem",
            text_transform="uppercase",
            letter_spacing="0.12em",
            color="#64748b",
            font_weight="600",
        ),
        rx.heading(
            value,
            size="7",
            color="#0f172a",
            font_family="'Manrope', 'Trebuchet MS', sans-serif",
        ),
        spacing="2",
        padding="1.15rem 1.2rem",
        border_radius="22px",
        background="rgba(255, 255, 255, 0.82)",
        border="1px solid rgba(148, 163, 184, 0.16)",
        box_shadow="0 14px 34px rgba(15, 23, 42, 0.05)",
        width="100%",
        align="start",
    )


def section_panel(title: str, subtitle: str, *children) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.box(
                rx.heading(
                    title,
                    size="6",
                    color="#0f172a",
                    font_family="'Manrope', 'Trebuchet MS', sans-serif",
                ),
                rx.text(
                    subtitle,
                    color="#64748b",
                    font_size="0.95rem",
                    line_height="1.6",
                    max_width="42rem",
                ),
                spacing="1",
                width="100%",
            ),
            *children,
            spacing="4",
            width="100%",
            align="stretch",
        ),
        padding="1.45rem",
        border_radius="28px",
        background="rgba(255, 255, 255, 0.88)",
        border="1px solid rgba(148, 163, 184, 0.18)",
        box_shadow="0 18px 40px rgba(15, 23, 42, 0.06)",
        width="100%",
    )


def finding_row(finding: str) -> rx.Component:
    return rx.box(
        rx.text(
            finding,
            color="#0f172a",
            white_space="pre-wrap",
            line_height="1.55",
            font_size="0.95rem",
        ),
        padding="1rem 1.05rem",
        border_radius="18px",
        background="#fbfdff",
        border="1px solid rgba(226, 232, 240, 0.9)",
        width="100%",
    )


def code_panel(title: str, value, accent: str) -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.text(
                title,
                color="#0f172a",
                font_weight="700",
                font_size="0.96rem",
            ),
            rx.box(
                width="0.7rem",
                height="0.7rem",
                border_radius="999px",
                background=accent,
            ),
            align="center",
            justify="between",
            width="100%",
        ),
        rx.text_area(
            value=value,
            read_only=True,
            width="100%",
            min_height="460px",
            resize="vertical",
            background="#0b1220",
            color="#edf2f7",
            border="1px solid rgba(51, 65, 85, 0.9)",
            border_radius="20px",
            font_family="'IBM Plex Mono', 'Consolas', monospace",
            font_size="0.92rem",
            line_height="1.65",
            padding="1.05rem",
            box_shadow="inset 0 1px 0 rgba(255,255,255,0.03)",
        ),
        spacing="3",
        width="100%",
        align="stretch",
        flex="1 1 460px",
    )


def index():
    return rx.box(
        navbar(),
        rx.box(
            rx.vstack(
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "Trusted analysis, refined output",
                                color="#475569",
                                font_size="0.83rem",
                                font_weight="600",
                                letter_spacing="0.08em",
                                text_transform="uppercase",
                            ),
                            padding="0.45rem 0.75rem",
                            border_radius="999px",
                            background="rgba(255, 255, 255, 0.62)",
                            border="1px solid rgba(148, 163, 184, 0.16)",
                        ),
                        rx.heading(
                            "Review code in a workspace that feels ready for production.",
                            size="8",
                            color="#0f172a",
                            font_family="'Manrope', 'Trebuchet MS', sans-serif",
                            line_height="1.08",
                            max_width="44rem",
                        ),
                        rx.text(
                            "Upload a Python file, inspect structural findings, and compare your source with an LLM-polished revision in one calm, readable layout.",
                            color="#475569",
                            font_size="1rem",
                            max_width="42rem",
                            line_height="1.75",
                        ),
                        rx.flex(
                            rx.box(
                                rx.text("Parser", color="#64748b", font_size="0.82rem"),
                                rx.text("AST + style checks", color="#0f172a", font_weight="600"),
                                spacing="1",
                            ),
                            rx.box(
                                rx.text("Review", color="#64748b", font_size="0.82rem"),
                                rx.text("LLM guidance + corrected code", color="#0f172a", font_weight="600"),
                                spacing="1",
                            ),
                            gap="2rem",
                            wrap="wrap",
                            width="100%",
                        ),
                        spacing="3",
                        align="start",
                    ),
                    width="100%",
                    padding="2rem",
                    border_radius="32px",
                    background=(
                        "linear-gradient(145deg, rgba(255,255,255,0.92) 0%, rgba(248,250,252,0.9) 100%)"
                    ),
                    border="1px solid rgba(148, 163, 184, 0.18)",
                    box_shadow="0 24px 52px rgba(15, 23, 42, 0.08)",
                ),
                rx.flex(
                    stat_card("Errors", CodeState.error_count, "#ef4444"),
                    stat_card("Warnings", CodeState.warning_count, "#f59e0b"),
                    stat_card("Notes", CodeState.info_count, "#3b82f6"),
                    stat_card("Lines", CodeState.line_count, "#94a3b8"),
                    wrap="wrap",
                    gap="1rem",
                    width="100%",
                ),
                section_panel(
                    "Source",
                    "Upload a Python file or paste code directly into the workspace.",
                    rx.upload(
                        rx.vstack(
                            rx.text(
                                "Drop a Python file here",
                                font_size="1rem",
                                font_weight="600",
                                color="#0f172a",
                            ),
                            rx.text(
                                "or browse from your device",
                                color="#64748b",
                                font_size="0.94rem",
                            ),
                            spacing="2",
                            align="center",
                            width="100%",
                        ),
                        id=UPLOAD_ID,
                        accept={"text/plain": [".py", ".pyi", ".txt"]},
                        max_files=1,
                        multiple=False,
                        width="100%",
                        padding="2rem 1rem",
                        border="1.5px dashed rgba(148, 163, 184, 0.62)",
                        border_radius="22px",
                        background="#f8fafc",
                    ),
                    rx.flex(
                        rx.foreach(
                            rx.selected_files(UPLOAD_ID),
                            lambda name: rx.badge(
                                name,
                                radius="full",
                                color_scheme="blue",
                                variant="soft",
                                size="3",
                            ),
                        ),
                        rx.spacer(),
                        rx.button(
                            "Load file",
                            on_click=CodeState.handle_upload(
                                rx.upload_files(upload_id=UPLOAD_ID)
                            ),
                            background="#0f172a",
                            color="white",
                            border_radius="999px",
                            padding="0.7rem 1rem",
                        ),
                        width="100%",
                        align="center",
                        gap="0.75rem",
                        wrap="wrap",
                    ),
                    rx.text(
                        CodeState.syntax_message,
                        color="#334155",
                        font_size="0.95rem",
                    ),
                    rx.text_area(
                        value=CodeState.code_input,
                        on_change=CodeState.update_code_input,
                        placeholder="Paste Python code here.",
                        width="100%",
                        min_height="360px",
                        resize="vertical",
                        background="#0b1220",
                        color="#edf2f7",
                        border="1px solid rgba(51, 65, 85, 0.9)",
                        border_radius="22px",
                        font_family="'IBM Plex Mono', 'Consolas', monospace",
                        font_size="0.94rem",
                        line_height="1.65",
                        padding="1.05rem",
                    ),
                    rx.flex(
                        rx.button(
                            "Run review",
                            on_click=CodeState.analyze,
                            loading=CodeState.is_loading,
                            background="#0f172a",
                            color="white",
                            border_radius="999px",
                            size="3",
                            padding="0.72rem 1.05rem",
                        ),
                        rx.button(
                            "Use sample",
                            on_click=CodeState.load_sample,
                            variant="soft",
                            color_scheme="gray",
                            border_radius="999px",
                            size="3",
                        ),
                        rx.button(
                            "Clear",
                            on_click=CodeState.clear_workspace,
                            variant="outline",
                            color_scheme="gray",
                            border_radius="999px",
                            size="3",
                        ),
                        gap="0.75rem",
                        wrap="wrap",
                    ),
                    rx.cond(
                        CodeState.error_message != "",
                        rx.box(
                            rx.text(
                                CodeState.error_message,
                                color="#991b1b",
                                font_weight="600",
                            ),
                            padding="0.9rem 1rem",
                            border_radius="18px",
                            background="#fef2f2",
                            border="1px solid #fecaca",
                            width="100%",
                        ),
                    ),
                ),
                rx.cond(
                    CodeState.review_ready,
                    rx.vstack(
                        section_panel(
                            "Analysis",
                            "A structured view of local findings before the model response.",
                            rx.text(
                                CodeState.review_summary,
                                color="#0f172a",
                                font_weight="600",
                            ),
                            rx.flex(
                                stat_card("Non-empty lines", CodeState.non_empty_lines, "#2563eb"),
                                stat_card("Functions", CodeState.function_count, "#0f172a"),
                                stat_card("Classes", CodeState.class_count, "#6366f1"),
                                stat_card("Imports", CodeState.import_count, "#9333ea"),
                                wrap="wrap",
                                gap="1rem",
                                width="100%",
                            ),
                            rx.cond(
                                CodeState.has_findings,
                                rx.vstack(
                                    rx.foreach(CodeState.findings, finding_row),
                                    spacing="3",
                                    width="100%",
                                ),
                                rx.box(
                                    rx.text(
                                        "No static findings were reported for this file.",
                                        color="#166534",
                                        font_weight="600",
                                    ),
                                    padding="1rem",
                                    border_radius="18px",
                                    background="#f0fdf4",
                                    border="1px solid #bbf7d0",
                                ),
                            ),
                        ),
                        section_panel(
                            "AI Review",
                            "Read the model feedback and compare the original code with the revised output.",
                            rx.flex(
                                rx.badge(
                                    CodeState.llm_status,
                                    radius="full",
                                    variant="soft",
                                    color_scheme="gray",
                                    size="3",
                                ),
                                rx.badge(
                                    CodeState.llm_provider,
                                    radius="full",
                                    variant="soft",
                                    color_scheme="gray",
                                    size="3",
                                ),
                                gap="0.75rem",
                                wrap="wrap",
                            ),
                            rx.box(
                                rx.markdown(CodeState.llm_review),
                                padding="1.1rem",
                                border_radius="20px",
                                background="#fbfdff",
                                border="1px solid rgba(226, 232, 240, 0.95)",
                                width="100%",
                            ),
                            rx.flex(
                                code_panel("Input code", CodeState.code_input, "#2563eb"),
                                code_panel(
                                    "LLM corrected code",
                                    CodeState.corrected_code,
                                    "#0f172a",
                                ),
                                direction="row",
                                wrap="wrap",
                                gap="1rem",
                                width="100%",
                                align="stretch",
                            ),
                        ),
                        spacing="1.2rem",
                        width="100%",
                    ),
                ),
                spacing="1.2rem",
                width="100%",
                max_width="1240px",
                align="stretch",
            ),
            width="100%",
            min_height="100vh",
            padding="1.5rem",
            background=(
                "radial-gradient(circle at top left, rgba(148, 163, 184, 0.12), transparent 28%), "
                "radial-gradient(circle at bottom right, rgba(15, 23, 42, 0.06), transparent 24%), "
                "linear-gradient(180deg, #f8fafc 0%, #f4f7fb 52%, #eef2f7 100%)"
            ),
        ),
    )


app = rx.App()
app.add_page(index, title="AI Code Reviewer")
