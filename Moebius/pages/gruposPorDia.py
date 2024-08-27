import reflex as rx
from ..UI.base import base_page
from .. import navigation

@rx.page(route=navigation.routes.GRUPOS_ROUTE)
def gruposPorDia() -> rx.Component:
    myChild= rx.vstack(
        rx.heading("Grupos Por Día", size="9", align="center", as_="h1"),
        text_align="center",
        align="center",
        justify="center",
        id="myChild", 

    ),
    return base_page(myChild)