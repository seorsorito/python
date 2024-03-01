import mysql.connector
from tkinter import messagebox
from tkinter import *

nombre_BBDD="" #para almacenar el nombre de la base de datos que sacamos en conexiones
def almacena(nom_BBDD):
    global nombre_BBDD
    nombre_BBDD=nom_BBDD

def Crear(*args):
    global nombre_BBDD
    miConexion= mysql.connector.connect(host="localhost",database=nombre_BBDD,user="root",password="1234")
    miCursor=miConexion.cursor()
    '''miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'"+ mi_Nombre.get()+ "','"+mi_Apellido.get()
                     + "','"+mi_Password.get()+ "','"+mi_Direccion.get()
                     + "','"+CuadroComentario.get("1.0",END)+"')")'''
    #consulta parametrizada
    #los_datos=mi_Nombre.get(),mi_Apellido.get(),mi_Password.get(),mi_Direccion.get(),CuadroComentario.get("1.0",END)

    los_datos_lista=[]
    for campo in args:
        if type(campo)==str:
            los_datos_lista.append(campo)
        else:
            los_datos_lista.append(campo.get())
    
    los_datos=tuple(los_datos_lista) #convertimos la lista en tupla para el metodo execute

    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,%s,%s,%s,%s,%s)",(los_datos))
    #---------------------------------------------
    miConexion.commit()

    messagebox.showinfo("CRUD","Registrado correctamente")

def Read(Id,*args):
    global nombre_BBDD
    miConexion= mysql.connector.connect(host="localhost",database=nombre_BBDD,user="root",password="1234")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + Id)

    Usuarios=miCursor.fetchall()

    pos_array=1

    for campo in args:
        for valor in Usuarios:
            if type(campo)==Text:
                campo.insert(1.0,valor[pos_array])
            else:
                campo.set(valor[pos_array])
            pos_array+=1


    miConexion.commit()

def Actualizar(Id,*args):
    global nombre_BBDD
    miConexion= mysql.connector.connect(host="localhost",database=nombre_BBDD,user="root",password="1234")
    miCursor=miConexion.cursor()
    '''miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE='"+mi_Nombre.get()+"',APELLIDO='"+mi_Apellido.get()+"',PASSWORD='"+mi_Password.get()
                     +"',DIRECCION='"+mi_Direccion.get()+"',COMENTARIOS='"+CuadroComentario.get("1.0",END)+"'WHERE ID="+mi_ID.get())'''
    #los_datos=mi_Nombre.get(),mi_Apellido.get(),mi_Password.get(),mi_Direccion.get(),CuadroComentario.get("1.0",END)
    los_datos_lista=[]
    for campo in args:
        if type(campo)==str:
            los_datos_lista.append(campo)
        else:
            los_datos_lista.append(campo.get())
    
    los_datos=tuple(los_datos_lista) #convertimos la lista en tupla para el metodo execute

    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE=%s,APELLIDO=%s,PASSWORD=%s,DIRECCION=%s,COMENTARIOS=%s WHERE ID=" +Id,(los_datos))
    miConexion.commit()

    messagebox.showinfo("CRUD","Actualizado correctamente")

def Borrar(Id,*args):
    global nombre_BBDD
    miConexion= mysql.connector.connect(host="localhost",database=nombre_BBDD,user="root",password="1234")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+Id)

    miConexion.commit()
    messagebox.showinfo("CRUD","Usuario eliminado")