import reflex as rx
from ..UI.base import base_page
from .. import navigation
from .. import context


class ausenciaState(rx.State):
    form_data: dict={}
    
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data

class fueraDeListaState(rx.State):
    form_data: dict={}
    
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data

@rx.page(route=navigation.routes.NOTIFICACIONES_ROUTE)  
def notificaciones() -> rx.Component:
    ausenciasForm=rx.form  (
        rx.vstack(
                rx.heading("Ausente clases consecutivas:", 
                    as_="h2", 
                    padding= "5% 0", 
                    required=True 
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
                rx.select([], 
                  placeholder="Grupo", 
                  label="grupo", 
                  name="grupo", 
                  width="100%"
                ),  
                rx.input(
                    placeholder="Nombre y Apellido",
                    name="participante",
                    required=True,
                    width="100%"
                ),
                rx.button("Submit", 
                    type="submit",
                ),
            ),
            on_submit=ausenciaState.handle_submit,
            reset_on_submit=True,
        ),
    fueraDeListaForm=rx.form(
        rx.vstack(
                rx.heading("Fuera de Lista:", 
                    as_="h2",
                    padding= "5% 0", 
                    required=True 
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
                rx.select([], 
                  placeholder="Grupo", 
                  label="grupo", 
                  name="grupo", 
                  width="100%"
                ),  
                rx.input(
                    placeholder="Nombre y Apellido",
                    name="participante",
                    required=True,
                    width="100%"
                ),
                rx.button("Submit", 
                    type="submit",
                ),
            ),
            on_submit=fueraDeListaState.handle_submit,
            reset_on_submit=True,
        ),
    myChild= rx.vstack(
        rx.heading("Notificaciones", as_="h1", size="9"),

        rx.tabs.root(
            rx.tabs.list(
                rx.tabs.trigger("Ausencias", value="tab1"),
                rx.tabs.trigger("Fuera de Lista", value="tab2"),
                size="2"
            ),
        rx.tabs.content(
            rx.desktop_only(
                rx.box(
                    ausenciasForm,
                    width="20vw"
                ),
            ),
            rx.mobile_and_tablet(
                rx.box(
                    ausenciasForm,
                    width="60vw"
                ),
            ),
            value="tab1",
        ),
        rx.tabs.content(
            rx.desktop_only(
                rx.box(
                    fueraDeListaForm,
                    width="20vw"
                ),
            ),
            rx.mobile_and_tablet(
                rx.box(
                    fueraDeListaForm,
                    width="60vw"
                ),
            ),
            value="tab2",
            ),

        ),
        spacing="2",
        align="center",
        #justify="center",
        min_height="85vh",
        id="myChild", 
    ),
    return base_page(myChild)