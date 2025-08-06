import flet as ft

from app.screens.BuscarRuta import BuscarRutaScreen
from app.screens.login import LoginScreen
from app.screens.register import RegisterScreen
from app.screens.home import HomeScreen
from app.screens.notifications import NotificationsScreen
from app.screens.map import MapScreen
from app.screens.history import HistoryScreen
from app.screens.menu import MenuScreen

def main(page: ft.Page):
    page.title = "Mobil Rute"
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change(route):
        page.views.clear()

        if page.route == "/login":
            page.views.append(LoginScreen(page))
        elif page.route == "/register":
            page.views.append(RegisterScreen(page))
        elif page.route == "/home":
            page.views.append(HomeScreen(page))
        elif page.route == "/notifications":
            page.views.append(NotificationsScreen(page))
        elif page.route == "/map":
            page.views.append(MapScreen(page))
        elif page.route == "/history":
            page.views.append(HistoryScreen(page))
        elif page.route == "/menu":
            page.views.append(MenuScreen(page))
        elif route == "/buscar":
            page.views.append(BuscarRutaScreen(page))

        page.update()

    page.on_route_change = route_change
    page.go("/login")  # Cambia a "/home" si quieres ir directo a la pantalla principal

ft.app(target=main)
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)

    import os
    from dotenv import load_dotenv

    if os.environ.get("RENDER") != "true":
        load_dotenv()

