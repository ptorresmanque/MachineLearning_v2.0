from lxml import etree
import sqlite3
import numpy as np

conn = sqlite3.connect('ej.db')

c = conn.cursor()
c.execute('''CREATE TABLE features
             (id integer primary key asc, ancho integer, alto integer, area integer, clase integer)''')
for i in range(1, 12):

    doc = etree.parse("imagen_"+str(i)+".xml")

    #print etree.tostring(doc,pretty_print=True ,xml_declaration=True, encoding="utf-8")

    raiz = doc.getroot()

    obj = raiz[4] # primer object
    for obj in raiz[4:]:
        if obj[1].text != "1": #el xml tambien incluye los bounding box eliminados recientes, por ello hay que saltarselos
            id = obj[7] #espacio donde se encuentra la ID del bounding box

            poligono = obj[9]

            sup_izq = poligono[1] # punto de la esquina superior izquierda


            sup_der = poligono[2] # punto de la esquina superior derecha


            inf_izq = poligono[4] # punto de la esquina inferior izquierda


            inf_der = poligono[3] # punto de la esquina inferior derecha
            for i in range(16): ####aqui creamos un ciclo que crea 16 clases positivas a partir de una modificando los vertices

                rd1 = np.random.randint(-2, 2)
                rd2 = np.random.randint(-2, 2)
                rd3 = np.random.randint(-2, 2)
                rd4 = np.random.randint(-2, 2)

                ancho = abs((int(sup_der[0].text)+ rd1) - (int(sup_izq[0].text) + rd2))
                print(ancho)
                alto = abs((int(sup_der[1].text) + rd3) - (int(inf_der[1].text)) + rd4)
                print(alto)
                area = ancho * alto

                c.execute("insert into features (ancho, alto, area, clase) values (?, ?, ?, ?)",
                          (ancho, alto, area, 1))
                conn.commit()



for row in c.execute('SELECT * FROM features'): # mostrar base de datos
    print (row)

conn.close()