import reflex as rx
from .model import grupoModel
import asyncio
from sqlmodel import select
from typing import List



class nuevoGrupoState(rx.State):
    form_data: dict={}
    entries: List ["grupoModel"] = []
    
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



    def list_groups(self):
        with rx.session() as session:
            entries= session.exec(
                select(grupoModel)
            ).all()
            self.entries = entries