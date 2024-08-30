import reflex as rx

from .. import navigation

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:   
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                            src="/logo.jpeg",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                            ),
                            href=navigation.routes.HOME_ROUTE
                        ),
                    rx.link(
                        rx.heading(
                            "Moebius 1.0", size="7", weight="bold"
                            ),
                        align_items="center",
                        href=navigation.routes.HOME_ROUTE
                        ), 
                    ),
                rx.hstack(
                    navbar_link("Home", navigation.routes.HOME_ROUTE),
                    navbar_link("Grupos", navigation.routes.GRUPOS_ROUTE),
                    navbar_link("Nuevo Grupo", navigation.routes.NUEVO_GRUPOS_ROUTE),
                    navbar_link("Listas", navigation.routes.LISTAS_ROUTE),
                    navbar_link("Notificaciones", navigation.routes.NOTIFICACIONES_ROUTE),
                    #navbar_link("Pagos", "/#"),
                    #navbar_link("Billetera", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),

                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpeg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Moebius 1.0", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home",
                            on_click=navigation.NavState.toHome),
                        rx.menu.item("Grupos",
                            on_click=navigation.NavState.toGrupos),
                        rx.menu.item("Nuevo Grupo",
                            on_click=navigation.NavState.toNuevoGrupo),
                        rx.menu.item("Listas",
                            on_click=navigation.NavState.toListas),
                        rx.menu.item("Notificaciones",
                            on_click=navigation.NavState.toNotificaciones),                        
                        #rx.menu.item("Pagos"),
                        #rx.menu.item("Billetera"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
        id="navbarPrincipal",
    )