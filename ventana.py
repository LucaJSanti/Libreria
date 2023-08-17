import tkinter
import sqlite3
import funciones

conector = sqlite3.connect("base1.db")
cursor = conector.cursor()

def resultado():
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)


vt = tkinter.Tk()
vt.geometry("700x300")

et = tkinter.Label(vt,text = "ejemplo 1", bg="lightblue")
boton = tkinter.Button(vt, text="boton", padx=40, command=funciones.filtro)

entradatexto = tkinter.Entry(vt, font = "Helvetica 50")


conector.commit()
conector.close()

vt.mainloop()