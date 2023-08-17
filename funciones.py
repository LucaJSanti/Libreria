import sqlite3

def filtro():
    print("eliga tipo de articulo")
    tipo = input()
    print("eliga la marca del articulo")
    marca = input()
    print("eliga un rubro de articulos")
    rubro = input()
    filtro_tipo = ""
    filtro_marca = ""
    filtro_rubro = ""
    filtro = "SELECT * FROM articulos "
    
    if marca != '':
        filtro_marca = "[marca]='"+marca+"'"
    else:
        filtro_marca = ""

    if tipo != '':
        filtro_tipo = "[tipo]='"+tipo+"'"
    else:
        filtro_tipo = ""

    if rubro != '':
        filtro_rubro = "[rubro] = '"+rubro+"'"
    else:
        filtro_rubro = ""

    #construccion de la cadena filtro
    if filtro_marca != "":
        filtro = filtro + "WHERE " + filtro_marca
        if filtro_tipo != "":
            filtro = filtro + " AND " + filtro_tipo
        if filtro_rubro !="":
            filtro = filtro + " AND " + filtro_rubro


    elif filtro_tipo != "":
            filtro = filtro + "WHERE " + filtro_tipo
            if filtro_marca !="":
                filtro = filtro + " AND " + filtro_marca
            if filtro_rubro !="":
                filtro = filtro + " AND " + filtro_rubro


    elif filtro_rubro !="":
            filtro = filtro + "WHERE " + filtro_rubro
            if filtro_tipo !="":
                filtro = filtro + " AND " + filtro_tipo
            if filtro_marca !="":
                filtro = filtro + " AND " + filtro_marca


    return filtro


def precio_ganancia():
    conector = sqlite3.connect("base1.db")
    cursor = conector.cursor()
    
    cursor.execute("UPDATE articulos SET [precio venta]=[precio costo]+([precio costo]*0.21)+([precio costo]*0.5);")
    conector.commit()
    conector.close()


def aumentos():
    print("ingrese porcentaje de aumento: ")
    porcentaje = input()
    conector = sqlite3.connect("base1.db")
    cursor = conector.cursor()

    print("eliga tipo de articulo")
    tipo = input()
    print("eliga la marca del articulo")
    marca = input()
    print("eliga un rubro de articulos")
    rubro = input()
    filtro_tipo = ""
    filtro_marca = ""
    filtro_rubro = ""
    filtro = ""
    
    if marca != '':
        filtro_marca = "[marca]='"+marca+"'"
    else:
        filtro_marca = ""

    if tipo != '':
        filtro_tipo = "[tipo]='"+tipo+"'"
    else:
        filtro_tipo = ""

    if rubro != '':
        filtro_rubro = "[rubro] = '"+rubro+"'"
    else:
        filtro_rubro = ""

    #construccion de la cadena filtro
    if filtro_marca != "":
        filtro = filtro + "WHERE " + filtro_marca
        if filtro_tipo != "":
            filtro = filtro + " AND " + filtro_tipo
        if filtro_rubro !="":
            filtro = filtro + " AND " + filtro_rubro


    elif filtro_tipo != "":
            filtro = filtro + "WHERE " + filtro_tipo
            if filtro_marca !="":
                filtro = filtro + " AND " + filtro_marca
            if filtro_rubro !="":
                filtro = filtro + " AND " + filtro_rubro


    elif filtro_rubro !="":
            filtro = filtro + "WHERE " + filtro_rubro
            if filtro_tipo !="":
                filtro = filtro + " AND " + filtro_tipo
            if filtro_marca !="":
                filtro = filtro + " AND " + filtro_marca

    cursor.execute("UPDATE articulos SET [precio costo]=[precio costo]+([precio costo]*"+porcentaje+")"+filtro+"")
    print("UPDATE articulos SET [precio costo]=[precio costo]+([precio costo]*"+porcentaje+")"+filtro+"")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

    conector.commit()
    conector.close()



#aumentos()
#precio_ganancia()
#print(filtro())