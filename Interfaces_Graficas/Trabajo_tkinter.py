from tkinter import *

raiz = Tk ()

raiz.title("Python")

raiz.resizable(1,1) #admite dos parametros 0 para desavilitar (false) y 1 para habilitar(true)

raiz.iconbitmap("icono.ico") #para cambiar el icono, debe tener extension ico

#raiz.geometry("700x400") #cambia el tamañod de la pantalla, al meterle el tamaño al frame la interfaz de queda con ese tamaño

raiz.config(bg="green") #bg es background y es para cambiar el color 

#frame

miFrame=Frame()

miFrame.pack(side="top",anchor="n")#para meter el frame dentro de la raiz (empaquetado)

miFrame.config(bg="red")

miFrame.config(width="650",height="350") #tamaño frame



raiz.mainloop() #bucle infinito para mantener la ventana siempre operativa, siempre tiene que ser lo último
