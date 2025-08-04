import flet as ft
from app.services.auth_service import register_user

def RegisterScreen(page: ft.Page):

    name = ft.TextField(label="Nombre completo", width=300)
    email = ft.TextField(label="Correo", width=300)
    password = ft.TextField(label="Contraseña", password=True, width=300)
    message = ft.Text(value="", color="red")

    def on_register(e):
        success, msg = register_user(name.value, email.value, password.value)
        message.value = msg
        if success:
            page.go("/login")
        page.update()

    return ft.View(
        "/register",
        controls=[
            ft.Column([
                ft.Text("Registro de usuario", size=30),
                name,
                email,
                password,
                ft.ElevatedButton("Registrarse", on_click=on_register),
                message
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
