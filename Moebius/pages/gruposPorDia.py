import reflex as rx
from ..UI.base import base_page
from .. import navigation
from .. import context
from sqlmodel import Field
from datetime import datetime, timezone 


class grupoModel(rx.Model, table=True):
    actividad: str
    dia: str
    sede: str
    ciclo: str
    hora: str
    comentarios: str = Field(nullable=True)


class nuevoGrupoState(rx.State):
    form_data: dict={}
    
    async def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data
        with rx.session() as session:
            db_entry = grupoModel(
                **form_data    
            )
            session.add(db_entry)
            session.commit()
            yield

        self.did_submit=True


@rx.page(route=navigation.routes.GRUPOS_ROUTE)
def gruposPorDia() -> rx.Component:
    nuevoGrupoForm=rx.form  (
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
        ),
    myChild= rx.vstack(
        rx.heading("Grupos Por Día", size="9", align="center", as_="h1"),
        rx.desktop_only(
                rx.box(
                    nuevoGrupoForm,
                    width="20vw"
                ),
            ),
            rx.mobile_and_tablet(
                rx.box(
                    nuevoGrupoForm,
                    width="60vw"
                ),
            ),
        text_align="center",
        align="center",
        justify="center",
        id="myChild", 

    ),
    return base_page(myChild)