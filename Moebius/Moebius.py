"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from . import navigation, grupos

from . import pages

from .UI.base import base_page


class State(rx.State):
    """The app state."""

    ...



 

def index() -> rx.Component:
    # Welcome Page (Index)
    myChild= base_page(
        rx.heading("Moebius", size="72", align="center"),
        text_align="center",
        align="center",
        justify="center",
        id="myChild", 

    ),
    return (myChild)


app = rx.App()
app.add_page(index)
app.add_page(grupos.gruposPorDia_page, route=navigation.routes.NUEVO_GRUPOS_ROUTE)
app.add_page(grupos.grupos_list_page, route=navigation.routes.GRUPOS_ROUTE)

#app.add_page(pages.gruposPorDia, route=navigation.routes.GRUPOS_ROUTE)
app.add_page(pages.listas, route=navigation.routes.LISTAS_ROUTE)
app.add_page(pages.notificaciones, route=navigation.routes.NOTIFICACIONES_ROUTE)
