import sqlite3

conn = sqlite3.connect('ej.db')

c = conn.cursor()
f = open("data.txt","w")
for row in c.execute('SELECT ancho, alto, clase FROM features'): # mostrar base de datos
    print(row)
    f.write(' '.join(str(s) for s in row) + '\n')
conn.close()
f.close()