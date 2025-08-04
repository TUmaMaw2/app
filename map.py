import flet as ft

def MapScreen(page: ft.Page):
    def go_to(route):
        page.go(route)

    return ft.View(
        "/map",
        controls=[
            ft.AppBar(
                title=ft.Text("Mapa General"),
                bgcolor="#BBDEFB",  # Azul claro (equivale a BLUE_100)
                center_title=True
            ),
            ft.Column(
                controls=[
                    ft.Text("🗺️ Aquí se mostrará el mapa general del sistema", size=18),
                    ft.Text("🚏 Estaciones activas y rutas disponibles"),
                    ft.Divider(),
                    ft.ElevatedButton("🔙 Regresar al menú", on_click=lambda e: go_to("/home")),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.START
    )
