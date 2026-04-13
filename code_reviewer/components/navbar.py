import reflex as rx


def navbar():
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.heading(
                    "Code Review Studio",
                    size="7",
                    color="#0f172a",
                    font_family="'Manrope', 'Trebuchet MS', sans-serif",
                ),
                rx.text(
                    "Production-style review workspace for Python analysis and cleanups.",
                    color="#475569",
                    font_size="0.96rem",
                ),
                spacing="1",
                align="start",
            ),
            rx.box(
                rx.text(
                    "Live Review",
                    color="#0f172a",
                    font_weight="600",
                    font_size="0.88rem",
                ),
                padding="0.55rem 0.9rem",
                border_radius="999px",
                background="rgba(255, 255, 255, 0.88)",
                border="1px solid rgba(148, 163, 184, 0.28)",
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        width="100%",
        padding="1.2rem 1.6rem",
        background="rgba(248, 250, 252, 0.92)",
        border_bottom="1px solid rgba(148, 163, 184, 0.18)",
        backdrop_filter="blur(14px)",
    )
