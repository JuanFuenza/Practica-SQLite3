import sqlite3 as sql

def create_db():
    conn = sql.connect("streamers.db")
    conn.commit()
    conn.close()

def create_table():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE streamers (
            name text,
            followers integer,
            subs integer
        )"""
    )
    conn.commit()
    conn.close()

def insert_row(nombre, followers, subs):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def read_rows():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def insert_rows(streamer_list):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO streamers VALUES (?, ?, ?)"
    cursor.executemany(instruccion, streamer_list)
    conn.commit()
    conn.close()

def read_ordered(field):
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def search():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM streamers WHERE subs > 9800 ORDER BY subs DESC"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def update_fields():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE streamers SET followers=1200000 WHERE name like 'alexelcapo'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def delete_row():
    conn = sql.connect("streamers.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM streamers WHERE name like 'auronplay'"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # create_db()
    # create_table()
    # insert_row("Ibai", 7000000, 25000)
    # insert_row("Alexelcapo", 800000, 10000)
    # read_rows()
    # streamers = [
    #     ("Knekro", 500000, 9500),
    #     ("Cristinini", 3000000, 5500),
    #     ("AuronPlay", 8000000, 20000)
    # ]
    # insert_rows(streamers)
    # read_ordered("subs")
    # search()
    # update_fields()
    # delete_row()