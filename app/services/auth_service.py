from app.db.connection import get_connection

def register_user(name, email, password):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
            if cursor.fetchone():
                return False, "El correo ya está registrado."

            cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password)
            )
            conn.commit()
            return True, "Registro exitoso."
    finally:
        conn.close()

def login_user(email, password):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
            user = cursor.fetchone()
            if user:
                return True, "Inicio de sesión exitoso."
            else:
                return False, "Correo o contraseña incorrectos."
    finally:
        conn.close()
