import flet as ft

def HomeScreen(page: ft.Page):
    def go_to(route):
        page.go(route)

    profile_image = ft.CircleAvatar(
        content=ft.Image(
            src="https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y",
            width=60,
            height=60,
            fit=ft.ImageFit.COVER,
        ),
        radius=40,
    )

    return ft.View(
        "/home",
        controls=[
            ft.AppBar(
                title=ft.Text("Panel Principal"),
                leading=profile_image,
                # Opción 1: Usando string hexadecimal
                bgcolor="#90CAF9"
    ),
            ft.Column(
                [
                    ft.Text("Bienvenido a Mobil Rute", size=30, weight=ft.FontWeight.BOLD),
                    ft.ElevatedButton("📢 Notificaciones", on_click=lambda e: go_to("/notifications")),
                    ft.ElevatedButton("🗺️ Mapa General", on_click=lambda e: go_to("/map")),
                    ft.ElevatedButton("🔍 Buscar Ruta", on_click=lambda e: go_to("/search")),
                    ft.ElevatedButton("📜 Historial", on_click=lambda e: go_to("/history")),
                    ft.ElevatedButton("📋 Menú de Unidades", on_click=lambda e: go_to("/menu")),
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
