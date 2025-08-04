import flet as ft

def BuscarRutaScreen(page: ft.Page):
    def go_to(route):
        page.go(route)

    return ft.View(
        "/buscar",
        controls=[
            ft.AppBar(
                title=ft.Text("Buscar Ruta"),
                bgcolor="#C5CAE9",  # color suave
                center_title=True
            ),
            ft.Column(
                controls=[
                    ft.Text("🔍 Buscar ruta entre dos puntos", size=20),
                    ft.TextField(label="Origen", width=300),
                    ft.TextField(label="Destino", width=300),
                    ft.ElevatedButton("Buscar", on_click=lambda e: print("Buscar presionado")),
                    ft.ElevatedButton("⬅ Volver", on_click=lambda e: go_to("/home")),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.START
    )
