import sqlite3 as mysql

con = mysql.connect("form_crud.db")
cursor = con.cursor()
cursor.execute("DROP TABLE IF EXISTS users")

sql = """
    CREATE TABLE users (
        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "nome" TEXT,
        "idade" TEXT,
        "rua" TEXT,
        "cidade" TEXT,
        "numero" TEXT,
        "estado" TEXT,
        "email" TEXT
    )"""
cursor.execute(sql)
con.commit()
con.close()