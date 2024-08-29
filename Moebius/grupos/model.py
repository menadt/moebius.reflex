import reflex as rx
from sqlmodel import Field





class grupoModel(rx.Model, table=True):
    actividad: str
    dia: str
    sede: str
    ciclo: str
    hora: str
    comentarios: str = Field(nullable=True)
