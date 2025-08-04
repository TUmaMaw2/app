import flet as ft

def NotificationsScreen(page: ft.Page):
    def go_to(route):
        page.go(route)

    return ft.View(
        "/notifications",
        controls=[
            ft.AppBar(
                title=ft.Text("Notificaciones"),
                bgcolor="#BBDEFB",  # Hexadecimal en vez de ft.colors
                center_title=True
            ),
            ft.Column(
                controls=[
                    ft.Text("📬 Tienes nuevas alertas del sistema de transporte", size=18),
                    ft.Text("🚌 La ruta 23 está fuera de servicio temporalmente", color="#F44336"),  # rojo
                    ft.Text("⏰ La ruta 7 tiene un retraso de 10 minutos", color="#FFC107"),  # ámbar
                    ft.Divider(),
                    ft.ElevatedButton("🔙 Regresar al menú", on_click=lambda e: go_to("/home")),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.START
    )
