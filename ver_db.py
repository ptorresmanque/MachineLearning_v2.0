import sqlite3

conn = sqlite3.connect('ej.db')

c = conn.cursor()

for row in c.execute('SELECT * FROM features'): # mostrar base de datos
    print row

conn.close()