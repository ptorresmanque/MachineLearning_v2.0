import sqlite3
from random import randint, choice
import numpy as np


conn = sqlite3.connect('ej.db')

c = conn.cursor()

#OBTENIENDO TAMAnOS MAXIMOS MINIMOS Y PROMEDIO#
c.execute('SELECT MAX(alto) FROM features')
resultado = c.fetchone()
if resultado:
    altoMax = resultado[0]

c.execute('SELECT MIN(alto) FROM features')
resultado = c.fetchone()
if resultado:
    altoMin = resultado[0]

altoProm = abs((altoMax + altoMin) / 2)

#print altoMax , altoProm , altoMin
arrAlto = [altoMax , altoProm , altoMin]

c.execute('SELECT MAX(ancho) FROM features')
resultado = c.fetchone()
if resultado:
    anchoMax = resultado[0]

c.execute('SELECT MIN(ancho) FROM features')
resultado = c.fetchone()
if resultado:
    anchoMin = resultado[0]

anchoProm = abs((anchoMax + anchoMin) / 2)

anchoMaxProm = abs((anchoMax + anchoProm) / 2)

anchoMinProm = abs((anchoMin + anchoProm) / 2)

arrAncho = [anchoMax, anchoMaxProm, anchoProm, anchoMinProm, anchoMin]

####  CREANDO CLASES NEGATIVAS



for i in range(0,3):
    for j in range(0,5):
        for _ in range(10):
            negAncho = arrAncho[j]
            negAlto = arrAlto[i]
            rand_alto_max = int(negAlto * 1.5)
            rand_alto_min = int(negAlto * 0.5)
            r3 = rand_alto_max * 2

            rand_ancho_max = int(negAncho*1.5)
            rand_ancho_min = int(negAncho*0.5)
            r33 = rand_ancho_max * 2

            f1 = choice([np.random.randint(1, rand_alto_min), np.random.randint(rand_alto_max, r3)])
            f2 = choice([np.random.randint(1, rand_ancho_min), np.random.randint(rand_ancho_max, r33)])

            c.execute("insert into features (ancho, alto, area, clase) values (?, ?, ?, ?)",
                      (f2, f1, f2*f1, 0))





conn.commit()



conn.close()