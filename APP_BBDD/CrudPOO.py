from tkinter import *
from typing import Any, Literal
from Conexiones import *
from FuncionesCRUD import *
from tkinter import messagebox as MessageBox


class CrudPOO(Frame):

    def __init__(self,raiz):

        #---------------Variables de control------------------------------
    
        self.mi_ID=StringVar()
        self.mi_Nombre=StringVar()
        self.mi_Apellido=StringVar()
        self.mi_Password=StringVar()
        self.mi_Direccion=StringVar()

        #-----------barra de menu----------------------
        self.barramenu=Menu(raiz)
        raiz.config(menu=self.barramenu)
        super().__init__(raiz,width=300,height=300)
        self.master=raiz
        self.pack()

        self.MiframeBotones=Frame(raiz)
        self.MiframeBotones.pack()

        self.Crear_widgets()
        self.Crear_botones()
        self.Crear_BarraMenu()

    def Crear_widgets(self):
        self.ID=Label(self,text= "ID: ")
        self.ID.grid(row=0,column=0, sticky="w")
        #----------- 
        self.Nombre=Label(self,text= "Nombre: ")
        self.Nombre.grid(row=1,column=0, sticky="w")
        #----------- 
        self.Apellido=Label(self,text= "Apellido: ")
        self.Apellido.grid(row=2,column=0, sticky="w")
        #----------- 
        self.Password=Label(self,text= "Password: ")
        self.Password.grid(row=3,column=0, sticky="w")
        #----------- 
        self.Direccion=Label(self,text= "Direccion: ")
        self.Direccion.grid(row=4,column=0, sticky="w")
        #----------- 
        self.Comentarios=Label(self,text= "Comentarios: ")
        self.Comentarios.grid(row=5,column=0, sticky="w")
        #-----------    

        #cuadros 
        self.CuadroID=Entry(self, textvariable=self.mi_ID) 
        self.CuadroID.grid(row=0,column=1,padx=15,pady=6) 
        self.CuadroID.config(fg="red")
        #-----------
        self.CuadroNombre=Entry(self, textvariable=self.mi_Nombre) 
        self.CuadroNombre.grid(row=1,column=1,padx=15,pady=6) 
        self.CuadroNombre.config(fg="red")
        #-----------
        self.CuadroApellido=Entry(self, textvariable=self.mi_Apellido) 
        self.CuadroApellido.grid(row=2,column=1,padx=15,pady=6) 
        self.CuadroApellido.config(fg="red")
        #-----------
        self.CuadroPassword=Entry(self, textvariable=self.mi_Password) 
        self.CuadroPassword.grid(row=3,column=1,padx=15,pady=6) 
        self.CuadroPassword.config(show="*")
        #-----------
        self.CuadroDireccion=Entry(self, textvariable=self.mi_Direccion) 
        self.CuadroDireccion.grid(row=4,column=1,padx=15,pady=6) 
        self.CuadroDireccion.config(fg="red")
        #-----------
        self.CuadroComentario=Text(self,width=15,height=7) 
        self.CuadroComentario.grid(row=5,column=1,padx=15,pady=6) 
        self.CuadroComentario.config(fg="red")
        self.barravertical=Scrollbar(self,command=self.CuadroComentario.yview) 
        self.barravertical.grid(row=5,column=2, sticky="nsew")
        self. CuadroComentario.config(yscrollcommand=self.barravertical.set)
        #-----------
    def Crear_botones(self):
        BotonCrear=Button(self.MiframeBotones,text="Crear",command=lambda: Crear(self.mi_Nombre,self.mi_Apellido,self.mi_Password,self.mi_Direccion,self.CuadroComentario.get(1.0,END)))
        BotonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)
        #------------------------
        BotonLeer=Button(self.MiframeBotones,text="Leer",command=lambda: Read(self.mi_ID.get(),self.mi_Nombre,self.mi_Apellido,self.mi_Password,self.mi_Direccion,self.CuadroComentario))
        BotonLeer.grid(row=1,column=1,sticky="e",padx=10,pady=10)
        #------------------------
        BotonActualizar=Button(self.MiframeBotones,text="Actualizar",command=lambda: Actualizar(self.mi_ID.get(),self.mi_Nombre,self.mi_Apellido,self.mi_Password,self.mi_Direccion,self.CuadroComentario.get(1.0,END)))
        BotonActualizar.grid(row=1,column=2,sticky="e",padx=10,pady=10)
        #------------------------
        BotonBorrar=Button(self.MiframeBotones,text="Borrar",command=lambda: Borrar(self.mi_ID.get(),self.mi_Nombre,self.mi_Apellido,self.mi_Password,self.mi_Direccion,self.CuadroComentario.get(1.0,END)))
        BotonBorrar.grid(row=1,column=3,sticky="e",padx=10,pady=10)
    



    def Crear_BarraMenu(self):
        
        self.bbddMenu=Menu(self.barramenu,tearoff=0) #tearoff es para que no salga las barras divisorias
        self.bbddMenu.add_command(label="conectar", command=conectarbbdd)
        self.bbddMenu.add_command(label="salir",command=lambda: SalirApp(raiz)) #usamos lambda porque al recibir un parametro command actuará inmediatamente y no cuadno nosotros demos al boton

        self.borrarMenu=Menu(self.barramenu,tearoff=0)
        self.borrarMenu.add_command(label="borrar",command=lambda: LimpiarCampos(self.CuadroComentario,self.mi_ID,self.mi_Nombre,self.mi_Apellido,self.mi_Password,self.mi_Direccion))

        self.crudMenu=Menu(self.barramenu,tearoff=0)
        self.crudMenu.add_command(label="crear",command=lambda: Crear(self.mi_Nombre,self.mi_Apellido,self.mi_Password,self.mi_Direccion,self.CuadroComentario.get(1.0,END)))
        self.crudMenu.add_command(label="leer",command=lambda: Read(self.mi_ID.get(),self.mi_Nombre,self.mi_Apellido,self.mi_Password,self.mi_Direccion,self.CuadroComentario))
        self.crudMenu.add_command(label="actualizar",command=lambda: Actualizar(self.mi_ID.get(),self.mi_Nombre,self.mi_Apellido,self.mi_Password,self.mi_Direccion,self.CuadroComentario.get(1.0,END)))
        self.crudMenu.add_command(label="borrar",command=lambda: Borrar(self.mi_ID.get(),self.mi_Nombre,self.mi_Apellido,self.mi_Password,self.mi_Direccion,self.CuadroComentario.get(1.0,END)))

        self.ayudaMenu=Menu(self.barramenu,tearoff=0)
        self.ayudaMenu.add_command(label="Licencia",command=lambda:MessageBox.showinfo("Licencia","BBDD tkinter 2.0"))
        self.ayudaMenu.add_command(label="Acerca de...",command=lambda:MessageBox.showinfo("Acerca de","Victor Gayo programador"))


        self.barramenu.add_cascade(label="BBDD",menu= self.bbddMenu)
        self.barramenu.add_cascade(label="BORRAR",menu= self.borrarMenu)
        self.barramenu.add_cascade(label="CRUD",menu= self.crudMenu)
        self.barramenu.add_cascade(label="AYUDA",menu= self.ayudaMenu)


raiz=Tk()
app=CrudPOO(raiz)
app.mainloop()