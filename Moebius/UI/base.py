import reflex as rx

from .navbar import navbar


def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(   
            child,
            id="contenedorBase",
            #bg=rx.color("accent", 3),
            padding="1em",
            width="100%",
            ),
        rx.color_mode.button(position="bottom-right"),
        rx.logo(),
    )