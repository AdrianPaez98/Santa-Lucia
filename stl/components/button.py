import reflex as rx


def button(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(text),
        href= url
    )