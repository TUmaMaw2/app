import flet as ft

def MenuScreen(page: ft.Page):
    def go_to(route):
        page.go(route)

    # Campos para ingresar datos
    numero_unidad = ft.TextField(label="Número de unidad", width=300)
    nombre_ruta = ft.TextField(label="Nombre de la ruta", width=300)
    horario = ft.TextField(label="Horario", width=300)

    def guardar_datos(e):
        print(f"Número: {numero_unidad.value}, Ruta: {nombre_ruta.value}, Horario: {horario.value}")
        page.snack_bar = ft.SnackBar(ft.Text("✅ Datos guardados correctamente"))
        page.snack_bar.open = True
        page.update()

    return ft.View(
        "/menu",
        controls=[
            ft.AppBar(
                title=ft.Text("Menú de Rutas"),
                bgcolor="#BBDEFB",  # Azul claro
                center_title=True
            ),
            ft.Column(
                controls=[
                    ft.Text("📋 Ingresar datos de la unidad:", size=18, weight="bold"),
                    numero_unidad,
                    nombre_ruta,
                    horario,
                    ft.ElevatedButton("💾 Guardar", on_click=guardar_datos),
                    ft.ElevatedButton("⬅ Volver", on_click=lambda e: go_to("/home")),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ]
    )
