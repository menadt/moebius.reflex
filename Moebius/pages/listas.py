import reflex as rx
from ..UI.base import base_page
from .. import navigation


@rx.page(route=navigation.routes.LISTAS_ROUTE)
def listas() -> rx.Component:
    myChild= rx.vstack(
        rx.heading("Listas", size="9", align="center", as_="h1"),
        text_align="center",
        align="center",
        justify="center",
        id="myChild", 

    ),
    return base_page(myChild)