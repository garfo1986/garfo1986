import sqlite3

number=""

def create():
    conn=sqlite3.connect('alumnos.db')
    conn.commit()
    conn.close()

create()

def createtable():
    conn=sqlite3.connect('alumnos.db')
    cursor= conn.cursor()
    cursor.execute(
        """CREATE TABLE alumnostab(
            id integer PRIMARY KEY AUTOINCREMENT,
            NAME TEXT,
            LAST_NAME TEXT
        )
        """
    )
    conn.commit()
    conn.close()

createtable()

def addanitem(name, last_name):
    conn= sqlite3.connect('alumnos.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO alumnostab (name, last_name) VALUES('{name}', '{last_name}')")
    conn.commit()
    conn.close()


addanitem('Jason', 'parra')

def showitem():
    conn = sqlite3.connect('alumnos.db')
    cursor=conn.cursor()
    cursor.execute(f'SELECT * FROM alumnostab')
    datos=cursor.fetchmany()
    conn.commit
    conn.close()
    print(datos)

def searchitem():
    conn = sqlite3.connect('alumnos.db')
    cursor=conn.cursor()
    cursor.execute(f'SELECT * FROM alumnostab WHERE name="Laura"')
    datos=cursor.fetchmany()
    conn.commit
    conn.close()
    print(datos)


def addseveral(S_list):
    conn =sqlite3.connect('alumnos.db')
    cursor=conn.cursor()
    cursor.executemany(f"INSERT INTO alumnostab(name, last_name) VALUES(?,?)",S_list)
    conn.commit()
    conn.close()

students = [
    ('Laura','Taylor'),
    ('Rober','Patino'),
    ('Gelma', 'Silva'),
    ('Carlos','Marin'),
    ('lucas', 'taneda'),
    ('Sofia','Feria'),
    ('Martha','Parrado'),
    ('Hector', 'Cadena')
]
addseveral(students)
showitem()
searchitem()


