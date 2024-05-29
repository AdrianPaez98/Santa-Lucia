"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .components.navbar import navbar
import reflex as rx


from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        navbar(),
        border="2px",
        border_color="#ff2",

    )


app = rx.App()

app.add_page(
    index,
    title= 'U.E. Santa Lucia'
)
