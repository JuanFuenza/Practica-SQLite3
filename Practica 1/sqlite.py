import  sqlite3
from estudiantes import Estudiante

conn = sqlite3.connect('universidad.db')
c = conn.cursor()

def create_student_table():
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE IF NOT EXISTS estudiantes (
        matricula TEXT PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        promedio REAL)""")
    conn.close()

# c.execute("INSERT INTO estudiantes VALUES ('111', 'Roberto', 'Cruz', '9.5')")

est_1= Estudiante('222', 'Adriana', 'Cruz', 9.5)
est_2 = Estudiante('333', 'Fabian', 'Romero', 9.0)
est_3 = Estudiante('444', 'Alejandro', 'Cruz', 7.5)
est_4 = Estudiante('666', 'Robert', 'Barrera', 8)

# c.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)",
#   (est_.matricula, est_.nombre, est_.apellido, est_.promedio))

# c.execute("INSERT INTO estudiantes VALUES (:matricula, :nombre, :apellido, :promedio)", 
# {'matricula': est_2.matricula, 'nombre': est_2.nombre, 'apellido': est_2.apellido, 'promedio':est_2.promedio})

# c.execute("INSERT INTO estudiantes (matricula, nombre, apellido) VALUES (?, ?, ?)",
#   (est_3.matricula, est_3.nombre, est_3.apellido))

# many_students = [
#     (est_1.matricula, est_1.nombre, est_1.apellido, est_1.promedio),
#     (est_2.matricula, est_2.nombre, est_2.apellido, est_2.promedio),
#     (est_3.matricula, est_3.nombre, est_3.apellido, est_3.promedio),
#     (est_4.matricula, est_4.nombre, est_4.apellido, est_4.promedio)
# ]

# c.executemany("INSERT INTO estudiantes VALUES (?, ?, ?, ?)", many_students)

# conn.commit()
# c.execute("SELECT * FROM estudiantes WHERE apellido=?", ('Cruz',))
# estudiantes = c.fetchall()
# print(estudiantes)

def insertar_estudiante(student):
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("INSERT INTO estudiantes VALUES (?, ?, ?, ?)", 
              (student.matricula, student.nombre, student.apellido, student.promedio))
    conn.commit()
    conn.close()

def select_student(matricula):
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("SELECT FROM estudiantes WHERE matricula=?", (matricula,))
    estudiante = c.fetchone()
    conn.close()
    return estudiante


def update_prom(matricula, prom):
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("UPDATE estudiantes SET promedio=? WHERE matricula=?", 
              (prom, matricula))
    conn.commit()
    conn.close()


def delete_student(matricula):
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("DELETE estudiantes WHERE matricula=?", (matricula))
    conn.commit()
    conn.close()

def select_all():
    conn = sqlite3.connect('universidad.db')
    c = conn.cursor()
    c.execute("SELECT * FROM estudiantes")
    print(c.fetchall())
    conn.close()

select_all()

conn.close()