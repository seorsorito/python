from tkinter import *

raiz = Tk()

Miframe = Frame(raiz,height=350,width=600)
Miframe.pack()
Digitos=StringVar()
operacion=""
resultado = 0

#-------------------------------------------------------------------------------
Pantalla= Entry(Miframe,textvariable=Digitos,font="Arial 21")
Pantalla.grid(row=0,column=0,columnspan=4,pady=10)
Pantalla.config(background="black",fg="green",justify="right",width=15)
Digitos.set("0")

#-------------------------------------------------------------------------------------------------------
   
def Pulsacion_coma():

    contador = 0 

    for i in Digitos.get():

        if i == ".":
            contador+=1
    
    if contador == 0:
        Digitos.set(Digitos.get()+ ".")



def funcionBotones(numPulsado):
    
    global operacion 
    


    if operacion !="":
        Digitos.set(numPulsado)
        operacion=""
    else:
        if numPulsado == "0" and Digitos.get()=="0": #para evitar poner muchos 0 seguidos
            Digitos.set("0")
        elif numPulsado == "," and Digitos.get()=="0":
            Digitos.set(Digitos.get()+numPulsado)
            
        elif numPulsado != "0" and Digitos.get() == "0": #para quitar el 0 del inicio
            Digitos.set(numPulsado)
        elif Digitos.get() != "0": 
            Digitos.set(Digitos.get()+numPulsado)
        
def funcionsuma(num):
    global operacion #global es para incluir variables que estan fuera de la funcion
    global resultado
    

    resultado+= float(num) #dado que en la calculadora es texto

    if resultado.is_integer():
        
        Digitos.set(int(resultado))
        operacion= "suma"
    else:
        operacion= "suma"
        Digitos.set(resultado)
     

def funcionresta(num):
    global operacion 
    global resultado

    operacion="resta"
    resultado = resultado - int(num)
    Digitos.set(resultado)


def funcionigual():
    global resultado
    
    if (resultado+float(Digitos.get())).is_integer():

        Digitos.set(int(resultado+float(Digitos.get())))
        resultado=0 #para resetear
    else:
        
        Digitos.set(resultado+float(Digitos.get()))
        resultado=0
#-------------------------------------------------------------------------------


#---------------------------------------------------------------

porcentaje=Button(Miframe,text= "%",width=7 )
porcentaje.grid(row=1,column=0)

fraccion=Button(Miframe,text= "1/x",width=7 )
fraccion.grid(row=2,column=0)

ce=Button(Miframe,text= "CE",width=7 )
ce.grid(row=1,column=1)

cuadrado=Button(Miframe,text= "x²",width=7 )
cuadrado.grid(row=2,column=1)

borrar=Button(Miframe,text= "C",width=7 )
borrar.grid(row=1,column=2)

raizCuadrada=Button(Miframe,text= "√x²",width=7 )
raizCuadrada.grid(row=2,column=2)

quitar=Button(Miframe,text= "<x",width=7 )
quitar.grid(row=1,column=3)

dividir=Button(Miframe,text= "/",width=7 )
dividir.grid(row=2,column=3)

multiplicar=Button(Miframe,text= "X",width=7 )
multiplicar.grid(row=3,column=3)

restar=Button(Miframe,text= "-",width=7, command=lambda:funcionresta(Digitos.get()) )
restar.grid(row=4,column=3)

sumar=Button(Miframe,text= "+",width=7, command=lambda:funcionsuma(Digitos.get()))
sumar.grid(row=5,column=3)

igual=Button(Miframe,text= "=",width=7,command=lambda:funcionigual() )
igual.grid(row=6,column=3)

coma=Button(Miframe,text= ",",width=7,command=lambda:Pulsacion_coma())
coma.grid(row=6,column=2)

#-----------------------------------------------------------------------------

numero0=Button(Miframe,text= "0",width=7,command=lambda:funcionBotones("0"))
numero0.grid(row=6,column=1)
numero1=Button(Miframe,text= "1",width=7,command=lambda:funcionBotones("1"))
numero1.grid(row=5,column=0)
numero2=Button(Miframe,text= "2",width=7,command=lambda:funcionBotones("2"))
numero2.grid(row=5,column=1)
numero3=Button(Miframe,text= "3",width=7,command=lambda:funcionBotones("3"))
numero3.grid(row=5,column=2)
numero4=Button(Miframe,text= "4",width=7,command=lambda:funcionBotones("4"))
numero4.grid(row=4,column=0)
numero5=Button(Miframe,text= "5",width=7,command=lambda:funcionBotones("5"))
numero5.grid(row=4,column=1)
numero6=Button(Miframe,text= "6",width=7,command=lambda:funcionBotones("6"))
numero6.grid(row=4,column=2)
numero7=Button(Miframe,text= "7",width=7,command=lambda:funcionBotones("7")) #importante usar lambda para que funcione el boton
numero7.grid(row=3,column=0)
numero8=Button(Miframe,text= "8",width=7,command=lambda:funcionBotones("8"))
numero8.grid(row=3,column=1)
numero9=Button(Miframe,text= "9",width=7,command=lambda:funcionBotones("9"))
numero9.grid(row=3,column=2)
#--------------------------------------------------------------------------------------








raiz.mainloop()