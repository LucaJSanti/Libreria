import sqlite3
import funciones

conector = sqlite3.connect("base1.db")
#coneccion con la base
cursor = conector.cursor()

#cursor.execute("SELECT * FROM articulos")
#executemany inserta datos de lista
#cursor.executemany("INSERT INTO articulos VALUES (?,?,?,?,?,?,?)", arts)
#cursor.execute("INSERT INTO articulos VALUES (19,'lapiz1','lapices','bic','escolar',14,'')")
cursor.execute(funciones.filtro())
filas = cursor.fetchall()
for fila in filas:
    print(fila)

conector.commit()
#realiza acciones de la coneccion
conector.close()
#cierra la coneccion