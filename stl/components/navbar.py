import reflex as rx
from .button import button


class MouseOver(rx.State):
    def menu_open(self):
        pass


def navbar() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text(
                """Colegio \n
                Santa Lucia""",
                margin_left="20px",
                align='left'
            )
        ),
        rx.spacer(),

        rx.box(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        'Nuestro Colegio',
                        variant='surface',
                        border_radius='10px')
                ),
                rx.menu.content(
                    rx.menu.item(
                        'Quienes somos'
                    ),
                    rx.menu.item(
                        'Misión | Visión'
                    )
                )
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        'Admisión',
                        variant='surface',
                        border_radius='10px'
                    )
                ),
                rx.menu.content(
                    rx.menu.item(
                        'Preescolar'
                    ),
                    rx.menu.item(
                        'Primaria'
                    ),
                    rx.menu.item(
                        'Media-general'
                    )
                )
            ),
        ),
        # button("Youtube", "https://www.youtube.com/watch?v=n2YrGsXJC6Y&t=1582s"),
        margin_top="20px",
        spacing='6'
    )
