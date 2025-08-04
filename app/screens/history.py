import flet as ft

def HistoryScreen(page: ft.Page):
    def go_to(route):
        page.go(route)

    return ft.View(
        "/history",
        controls=[
            ft.AppBar(
                title=ft.Text("Historial de Rutas"),
                bgcolor="#BBDEFB",  # Azul claro en hexadecimal
                center_title=True
            ),
            ft.Column(
                controls=[
                    ft.Text("Aquí se mostrarán las rutas que has consultado."),
                    ft.ElevatedButton("⬅ Volver", on_click=lambda e: go_to("/home")),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ]
    )
