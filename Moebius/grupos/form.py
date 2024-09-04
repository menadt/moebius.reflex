import reflex as rx
from .state import nuevoGrupoState
from .. import context


def nuevoGrupo_form() -> rx.Component:
    return rx.form  (
        rx.vstack(
                rx.heading("Nuevo Grupo:", 
                    as_="h2", 
                    padding= "5% 0", 
                    required=True 
                ),
                  rx.select(context.ACTIVIDAD, 
                    placeholder="Actividad", 
                    label="Actividad", 
                    name="actividad", 
                    required=True, 
                    width="100%"
                ),  
                rx.select(context.DIAS, 
                    placeholder="Dia", 
                    label="Dia", 
                    name="dia", 
                    required=True, 
                    width="100%"
                ),  
                rx.select(context.SEDE, 
                  placeholder="Sede", 
                  label="Sede", 
                  name="sede", 
                  required=True, 
                  width="100%"
                ),  
                rx.select(context.CICLO, 
                  placeholder="Ciclo", 
                  label="Ciclo", 
                  name="ciclo", 
                  required=True, 
                  width="100%"
                ),
                rx.input( 
                  placeholder="Hora", 
                  label="Hora", 
                  name="hora", 
                  required=True, 
                  width="100%"
                ),   
                rx.input(
                    placeholder="Comentarios",
                    name="comentarios", 
                    required=False,
                    width="100%"
                ),
                rx.button("Submit", 
                    type="submit",
                ),
            ),
            on_submit=nuevoGrupoState.handle_submit,
            reset_on_submit=True,
        )