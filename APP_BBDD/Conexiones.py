import mysql.connector
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
from FuncionesCRUD import *

def conectarbbdd():
    nombre_BBDD=simpledialog.askstring("BBDD","Introduce el nombre de la BBDD")
    almacena(nombre_BBDD) #asi almacenamos la base de datos introducida para las funciones
    miconexion= mysql.connector.connect(host="localhost",database=nombre_BBDD,user="root",password="1234") #base_datos
    miCursor=miconexion.cursor()
    #para evitar dar error porque ya este creada la base de datos lo metemos en un try-except
    try:
        miCursor.execute('''

        CREATE TABLE DATOSUSUARIOS(
                
                ID INT AUTO_INCREMENT PRIMARY KEY,
                NOMBRE VARCHAR(50),
                APELLIDO VARCHAR(50),
                PASSWORD VARCHAR(50),
                DIRECCION VARCHAR(70),
                COMENTARIOS VARCHAR(120)        
        )
                        ''')
        
        messagebox.showinfo("BBDD","BBDD creada con éxito") #titulo y mensajes
    except:
        messagebox.showwarning("warning","BBDD ya creada") #titulo y mensajes

def SalirApp(raiz):
    valorsalida=messagebox.askquestion("Salir","Deseas salir de la aplicación?")
    if valorsalida =="yes":
        raiz.destroy()
    else:
        pass

def LimpiarCampos(*args): #con args podemos meter un numero indeterminado. Parametros siempre detras del args 
    for campo in args:
        if type(campo)==Text:
           campo.delete(1.0,END)
        else:
            campo.set("")
    