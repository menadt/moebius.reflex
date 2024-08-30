import reflex as rx
from ..UI.base import base_page
from . import form
from . import state

def grupos_list_page() -> rx.Component:
    mychild=rx.vstack(
        rx.heading("Grupos Por Día", 
                   size="9", 
                   align="center", 
                   as_="h1"
                   ),
        text_align="center",
        align="center",
        justify="center",
        )
    return base_page(mychild)
    


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