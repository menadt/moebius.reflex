import reflex as rx
from ..UI.base import base_page
from . import form


def gruposPorDia_page() -> rx.Component:
    myChild= rx.vstack(
        rx.heading("Grupos Por Día", size="9", align="center", as_="h1"),
        rx.desktop_only(
                rx.box(
                    form.gruposPorDia_form(),
                    width="20vw"
                ),
            ),
            rx.mobile_and_tablet(
                rx.box(
                    form.gruposPorDia_form(),
                    width="60vw"
                ),
            ),
        text_align="center",
        align="center",
        justify="center",
        id="myChild", 

    ),
    return base_page(myChild)