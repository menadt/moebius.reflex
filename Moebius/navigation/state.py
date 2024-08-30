import reflex as rx

from . import routes

class NavState(rx.State):

    def toHome(self):
        return rx.redirect(routes.HOME_ROUTE)
    
    def toGrupos(self):
        return rx.redirect(routes.GRUPOS_ROUTE)
    
    def toNuevoGrupo(self):
        return rx.redirect(routes.NUEVO_GRUPOS_ROUTE)
    

    def toListas(self):
        return rx.redirect(routes.LISTAS_ROUTE)
    
    def toNotificaciones(self):
        return rx.redirect(routes.NOTIFICACIONES_ROUTE)