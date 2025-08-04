import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="040422cYa",
        database="mobil_rute",
        cursorclass=pymysql.cursors.DictCursor
    )
