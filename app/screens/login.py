import flet as ft
from app.services.auth_service import login_user

def LoginScreen(page: ft.Page):

    email = ft.TextField(label="Correo", width=300)
    password = ft.TextField(label="Contraseña", password=True, width=300)
    message = ft.Text(value="", color="red")

    # Nota: aquí usamos 'e' como evento, y accedemos a page desde el closure exterior
    def on_login(e):
        success, msg = login_user(email.value, password.value)
        message.value = msg
        if success:
            page.go("/home")
        page.update()

    return ft.View(
        "/login",
        controls=[
            ft.Column([
                ft.Text("Inicio de sesión", size=30),
                email,
                password,
                ft.ElevatedButton("Iniciar sesión", on_click=on_login),
                message,
                ft.TextButton(
                    "¿No tienes cuenta? Regístrate",
                    on_click=lambda e: page.go("/register")
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER
    )
