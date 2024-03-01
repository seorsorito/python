from tkinter import *
from tkinter import messagebox
import mysql.connector

raiz = Tk()

#conexion creacion bbdd tenemos que realizarlo antes de los elementos para que se ejecute

def conectarbbdd():
    miconexion= mysql.connector.connect(host="localhost",database="base_datos",user="root",password="1234")
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

def SalirApp():
    valorsalida=messagebox.askquestion("Salir","Deseas salir de la aplicación?")
    if valorsalida =="yes":
        raiz.destroy()
    else:
        pass

def LimpiarCampos():
    mi_ID.set("")
    mi_Nombre.set("")
    mi_Apellido.set("")
    mi_Password.set("")
    mi_Direccion.set("")
    CuadroComentario.delete(1.0,END)

def Crear():
    miConexion= mysql.connector.connect(host="localhost",database="base_datos",user="root",password="1234")
    miCursor=miConexion.cursor()
    '''miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES (NULL,'"+ mi_Nombre.get()+ "','"+mi_Apellido.get()
                     + "','"+mi_Password.get()+ "','"+mi_Direccion.get()
                     + "','"+CuadroComentario.get("1.0",END)+"')")'''
    #consulta parametrizada
    los_datos=mi_Nombre.get(),mi_Apellido.get(),mi_Password.get(),mi_Direccion.get(),CuadroComentario.get("1.0",END)
    miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,%s,%s,%s,%s,%s)",(los_datos))
    #---------------------------------------------
    miConexion.commit()

    messagebox.showinfo("CRUD","Registrado correctamente")

def Read():
    miConexion= mysql.connector.connect(host="localhost",database="base_datos",user="root",password="1234")
    miCursor=miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + mi_ID.get())

    Usuarios=miCursor.fetchall()

    for i in Usuarios:
        mi_ID.set(i[0])
        mi_Nombre.set(i[1])
        mi_Apellido.set(i[2])
        mi_Password.set(i[3])
        mi_Direccion.set(i[4])
        CuadroComentario.insert("1.0",i[5])

    miConexion.commit()

def Actualizar():
    miConexion= mysql.connector.connect(host="localhost",database="base_datos",user="root",password="1234")
    miCursor=miConexion.cursor()
    '''miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE='"+mi_Nombre.get()+"',APELLIDO='"+mi_Apellido.get()+"',PASSWORD='"+mi_Password.get()
                     +"',DIRECCION='"+mi_Direccion.get()+"',COMENTARIOS='"+CuadroComentario.get("1.0",END)+"'WHERE ID="+mi_ID.get())'''
    los_datos=mi_Nombre.get(),mi_Apellido.get(),mi_Password.get(),mi_Direccion.get(),CuadroComentario.get("1.0",END)
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE=%s,APELLIDO=%s,PASSWORD=%s,DIRECCION=%s,COMENTARIOS=%s WHERE ID=" +mi_ID.get(),(los_datos))
    miConexion.commit()

    messagebox.showinfo("CRUD","Actualizado correctamente")

def Borrar():
    miConexion= mysql.connector.connect(host="localhost",database="base_datos",user="root",password="1234")
    miCursor=miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+mi_ID.get())

    miConexion.commit()
    messagebox.showinfo("CRUD","Usuario eliminado")

#---------------Variables de control------------------------------
    
mi_ID=StringVar()
mi_Nombre=StringVar()
mi_Apellido=StringVar()
mi_Password=StringVar()
mi_Direccion=StringVar()

#----------------------------------------------------------------------
#elementos del menu
barramenu=Menu(raiz)
raiz.config(menu=barramenu,width=300,height=300)
bbddMenu=Menu(barramenu,tearoff=0) #tearoff es para que no salga las barras divisorias
bbddMenu.add_command(label="conectar", command=conectarbbdd)
bbddMenu.add_command(label="salir",command=SalirApp)

borrarMenu=Menu(barramenu,tearoff=0)
borrarMenu.add_command(label="borrar",command=LimpiarCampos)

crudMenu=Menu(barramenu,tearoff=0)
crudMenu.add_command(label="crear",command=Crear)
crudMenu.add_command(label="leer",command=Read)
crudMenu.add_command(label="actualizar",command=Actualizar)
crudMenu.add_command(label="borrar",command=Borrar)

ayudaMenu=Menu(barramenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")


barramenu.add_cascade(label="BBDD",menu= bbddMenu)
barramenu.add_cascade(label="BORRAR",menu= borrarMenu)
barramenu.add_cascade(label="CRUD",menu= crudMenu)
barramenu.add_cascade(label="AYUDA",menu= ayudaMenu)
#------------------------------------------------------
Miframe= Frame(raiz, width=500,height=450)
Miframe.pack()


#nombres cuadros
ID=Label(Miframe,text= "ID: ")
ID.grid(row=0,column=0, sticky="w")
#----------- 
Nombre=Label(Miframe,text= "Nombre: ")
Nombre.grid(row=1,column=0, sticky="w")
#----------- 
Apellido=Label(Miframe,text= "Apellido: ")
Apellido.grid(row=2,column=0, sticky="w")
#----------- 
Password=Label(Miframe,text= "Password: ")
Password.grid(row=3,column=0, sticky="w")
#----------- 
Direccion=Label(Miframe,text= "Direccion: ")
Direccion.grid(row=4,column=0, sticky="w")
#----------- 
Comentarios=Label(Miframe,text= "Comentarios: ")
Comentarios.grid(row=5,column=0, sticky="w")
#-----------    

#cuadros 
CuadroID=Entry(Miframe, textvariable=mi_ID) 
CuadroID.grid(row=0,column=1,padx=15,pady=6) 
CuadroID.config(fg="red")
#-----------
CuadroNombre=Entry(Miframe, textvariable=mi_Nombre) 
CuadroNombre.grid(row=1,column=1,padx=15,pady=6) 
CuadroNombre.config(fg="red")
#-----------
CuadroApellido=Entry(Miframe, textvariable=mi_Apellido) 
CuadroApellido.grid(row=2,column=1,padx=15,pady=6) 
CuadroApellido.config(fg="red")
#-----------
CuadroPassword=Entry(Miframe, textvariable=mi_Password) 
CuadroPassword.grid(row=3,column=1,padx=15,pady=6) 
CuadroPassword.config(show="*")
#-----------
CuadroDireccion=Entry(Miframe, textvariable=mi_Direccion) 
CuadroDireccion.grid(row=4,column=1,padx=15,pady=6) 
CuadroDireccion.config(fg="red")
#-----------
CuadroComentario=Text(Miframe,width=15,height=7) 
CuadroComentario.grid(row=5,column=1,padx=15,pady=6) 
CuadroComentario.config(fg="red")
barravertical=Scrollbar(Miframe,command=CuadroComentario.yview) 
barravertical.grid(row=5,column=2, sticky="nsew")
CuadroComentario.config(yscrollcommand=barravertical.set)
#-----------

#colocacion de botones 

MiframeBotones=Frame(raiz)
MiframeBotones.pack()

BotonCrear=Button(MiframeBotones,text="Crear",command=Crear)
BotonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)
#------------------------
BotonLeer=Button(MiframeBotones,text="Leer",command=Read)
BotonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)
#------------------------
BotonActualizar=Button(MiframeBotones,text="Actualizar",command=Actualizar)
BotonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)
#------------------------
BotonBorrar=Button(MiframeBotones,text="Borrar",command=Borrar)
BotonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)
#------------------------

    
     
   




raiz.mainloop()