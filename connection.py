import pymysql
import os

def get_connection():
    print("==== DEBUG CONEXIÓN ====")
    print("DB_HOST:", os.environ.get("DB_HOST"))
    print("DB_USER:", os.environ.get("DB_USER"))
    print("DB_PASSWORD:", os.environ.get("DB_PASSWORD"))
    print("DB_NAME:", os.environ.get("DB_NAME"))
    print("DB_PORT:", os.environ.get("DB_PORT"))

    return pymysql.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port=int(os.environ.get("DB_PORT", 3306)),
        cursorclass=pymysql.cursors.DictCursor
    )
