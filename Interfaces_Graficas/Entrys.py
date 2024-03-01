from tkinter import *
from tkinter import messagebox as MessageBox

raiz = Tk()

Miframe= Frame(raiz, width=500,height=450)

Miframe.pack()
Variabletexto=StringVar()

cuadroTexto=Entry(Miframe, textvariable=Variabletexto) #crea cuado de texto para escribir en el y ademas hemos hecho que guarde el texto en una variable
cuadroTexto.grid(row=0,column=1,padx=15,pady=6) #usamos .grid para colocarlo como una tabla 
#padx es el uso de padding para mantener una distancia entre ese objeto y otros
cuadroTexto.config(fg="red") #en caso de querer cambiar caracteristicas se usa el .config
Nombrelabel=Label(Miframe,text= "Nombre: ")
Nombrelabel.grid(row=0,column=0, sticky="w") #sticky es para colocar los textos donde tu quieras por defecto estan centrados
#Nombrelabel.config(font=4)

cuadroApellido=Entry(Miframe) 
cuadroApellido.grid(row=1,column=1,padx=15,pady=6) 
Apellidolabel=Label(Miframe,text= "Apellido: " )
Apellidolabel.grid(row=1,column=0,sticky="w") 

cuadrocontraseña=Entry(Miframe) 
cuadrocontraseña.grid(row=2,column=1,padx=15,pady=6) 
cuadrocontraseña.config(show="*") #para que se vea * cuando se introduce
Contraseñalabel=Label(Miframe,text= "contraseña: " )
Contraseñalabel.grid(row=2,column=0,sticky="w") 

cuadroEmail=Entry(Miframe) 
cuadroEmail.grid(row=3,column=1,padx=15,pady=6) 
Emaillabel=Label(Miframe,text= "Email: " )
Emaillabel.grid(row=3,column=0,sticky="w") 

cuadroDireccion=Entry(Miframe) 
cuadroDireccion.grid(row=4,column=1,padx=15,pady=6) 
Direccionlabel=Label(Miframe,text= "Direccion: " )
Direccionlabel.grid(row=4,column=0,sticky="w") 

comentariolabel=Label(Miframe,text="comentario: ")
comentariolabel.grid(row=5,column=0)
cuadroopiniones=Text(Miframe,width=15,height=7) #se usan para textos de gran tamaño, se especifica el tamaño
cuadroopiniones.grid(row=5,column=1,padx=15,pady=6)
barravertical=Scrollbar(Miframe,command=cuadroopiniones.yview) #barra vertical para mover. Con comand decimos a quien afecta y yview para decir que es vertical
barravertical.grid(row=5,column=2, sticky="nsew") #con sticky hacemos la barra a la altura del cuadro de comentarios y puede usarse
cuadroopiniones.config(yscrollcommand=barravertical.set)

def funcionboton():
    #MessageBox.showinfo("saludo","hola desde tkinter")
    #Variabletexto.set("introduzca nombre")
    informacion= Variabletexto.get()
    MessageBox.showinfo("informacion",informacion)
    #cuadroopiniones.insert(INSERT,"Texto de ejemplo que se inserta")
botonEnviar=Button(raiz, text="Enviar",command=funcionboton) #hemos creado un boton directamente en la raiz 
botonEnviar.pack()

raiz.mainloop()
