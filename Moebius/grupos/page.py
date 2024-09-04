import reflex as rx
from ..UI.base import base_page
from . import form
from . import state, model


#def foreach_callback(text):
#    return rx.box(rx.text(text))

def grupo_list_item(grupo: model.grupoModel):

    return (rx.box(
        rx.text(grupo.actividad),
        rx.heading(grupo.sede),
        rx.heading(grupo.dia),
        rx.text(grupo.hora," | ", grupo.comentarios ),
        padding="1em"
        )
    )
    
def grupos_list_page() -> rx.Component:
    mychild=rx.vstack(
        rx.heading("Grupos Por Día", 
                   size="9", 
                   align="center", 
                   as_="h1"
                   ),
 #       rx.foreach(["abc", "abc"],foreach_callback),
        rx.foreach(state.nuevoGrupoState.entries,grupo_list_item),
        text_align="center",
        align="center",
        justify="center",
        )
    return base_page(mychild)
    


def nuevoGrupo_page() -> rx.Component:
    myChild= rx.vstack(
        rx.heading("Nuevo Grupo", size="9", align="center", as_="h1"),
        rx.desktop_only(
                rx.box(
                    form.nuevoGrupo_form(),
                    width="20vw"
                ),
            ),
            rx.mobile_and_tablet(
                rx.box(
                    form.nuevoGrupo_form(),
                    width="60vw"
                ),
            ),
        text_align="center",
        align="center",
        justify="center",
        id="myChild", 

    ),
    return base_page(myChild)


 
