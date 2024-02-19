from tkinter import * 

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

        boton7 = self.colocar_boton(7)
        boton8 = self.colocar_boton(8)
        boton9 = self.colocar_boton(9)
        botonDiv = self.colocar_boton("/", mostrar = False)

        #---------------------------------------------

        boton4 = self.colocar_boton(4)
        boton5 = self.colocar_boton(5)
        boton6 = self.colocar_boton(6)
        botonMul = self.colocar_boton(u"\u00D7") #con caracter unicode
        botonMul.config(text="x") #una forma de que aparezca la x en pantalla pero que la funcion eval actue

        #---------------------------------------------

        boton1 = self.colocar_boton(1)
        boton2 = self.colocar_boton(2)
        boton3 = self.colocar_boton(3)
        botonRest = self.colocar_boton("-", mostrar = False)

        #---------------------------------------------
        boton0 = self.colocar_boton(0)
        botonComa = self.colocar_boton(".") #no tiene la variable mostrar porque quiero que se muestre en pantalla
        botonIgual = self.colocar_boton("=", mostrar = False)
        botonMas = self.colocar_boton("+")

        #---------------------------------------------

        
        Botones= [boton7,boton8,boton9,botonDiv,boton4,boton5,boton6,botonMul,boton1,boton2,boton3,botonRest,boton0,botonComa,botonIgual,botonMas]

        contador=0

        for fila in range(1,5):
            for columna in range(4):
                Botones[contador].grid(row=fila,column=columna)
                contador+=1

    def colocar_boton(self,valor,mostrar=True,ancho=9,alto=1):
        return Button(self.ventana,text=valor,width=ancho, height=alto, font=("Helvetica",9),
                      command=lambda:self.pulsaciones_teclas(valor,mostrar))
    def pulsaciones_teclas(self,valor,mostrar):
        if mostrar:
            self.operacion+=str(valor)
            self.mostrar_pantalla(valor)
        elif not mostrar and valor == "=":
            #self.operacion=re.sub(u"\u00D7","*",self.operacion) #para que funcione el multiplicar
            self.borrar_pantalla()
            self.mostrar_pantalla(str(eval(self.operacion)))
        else:
            pass
    def mostrar_pantalla(self,valor):
        self.Pantalla.insert(END,valor)
    def borrar_pantalla(self):
        self.Pantalla.delete(0,END) #se le da dos parametros porque puede borrar ciertas partes unicamente

        

Micalculadora= calculadora(raiz)

raiz.mainloop()