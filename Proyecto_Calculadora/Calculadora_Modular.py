from tkinter import * 

from Modulo_Calculadoras.Botones_Calculadora import *
raiz =Tk()

class calculadora:

    def __init__(self,ventana) :
        
        self.ventana = ventana 
        self.ventana.title("Calculadora POO")
        self.operacion=""

        #agregramos display

        self.Pantalla= Entry(ventana,font="Arial 21")

        #ubicar display (pantalla negra)

        self.Pantalla.grid(row=0,column=0,columnspan=4,pady=10)

        #formato display

        self.Pantalla.config(background="black",fg="green",justify="right",width=18)

        #creacion de botones 

        boton7 = colocar_boton(self,7)
        boton8 = colocar_boton(self,8)
        boton9 = colocar_boton(self,9)
        botonDiv = colocar_boton(self,"/")

        #---------------------------------------------

        boton4 = colocar_boton(self,4)
        boton5 = colocar_boton(self,5)
        boton6 = colocar_boton(self,6)
        botonMul = colocar_boton(self,u"\u00D7") #con caracter unicode
        botonMul.config(text="x") #una forma de que aparezca la x en pantalla pero que la funcion eval actue

        #---------------------------------------------

        boton1 = colocar_boton(self,1)
        boton2 = colocar_boton(self,2)
        boton3 = colocar_boton(self,3)
        botonRest = colocar_boton(self,"-", mostrar = False)

        #---------------------------------------------
        boton0 = colocar_boton(self,0)
        botonComa = colocar_boton(self,".") #no tiene la variable mostrar porque quiero que se muestre en pantalla
        botonIgual = colocar_boton(self,"=", mostrar = False)
        botonMas = colocar_boton(self,"+")

        #---------------------------------------------

        
        Botones= [boton7,boton8,boton9,botonDiv,boton4,boton5,boton6,botonMul,boton1,boton2,boton3,botonRest,boton0,botonComa,botonIgual,botonMas]

        contruir_botones(self,Botones,4,4)

Micalculadora= calculadora(raiz)

raiz.mainloop()