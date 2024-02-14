from tkinter import *

raiz = Tk()

Miframe = Frame(raiz,height=350,width=600)
Miframe.pack()

porcentaje=Button(Miframe,text= "%" )
porcentaje.grid(row=0,column=0)

fraccion=Button(Miframe,text= "1/x" )
fraccion.grid(row=1,column=0)

ce=Button(Miframe,text= "CE" )
ce.grid(row=0,column=1)

cuadrado=Button(Miframe,text= "x²" )
cuadrado.grid(row=1,column=1)

borrar=Button(Miframe,text= "C" )
borrar.grid(row=0,column=2)

raizCuadrada=Button(Miframe,text= "√x²" )
raizCuadrada.grid(row=1,column=2)

quitar=Button(Miframe,text= "<x" )
quitar.grid(row=0,column=3)

dividir=Button(Miframe,text= "/" )
dividir.grid(row=1,column=3)

multiplicar=Button(Miframe,text= "X" )
multiplicar.grid(row=2,column=3)

restar=Button(Miframe,text= "-" )
restar.grid(row=3,column=3)

sumar=Button(Miframe,text= "+" )
sumar.grid(row=4,column=3)

igual=Button(Miframe,text= "=" )
igual.grid(row=5,column=3)

coma=Button(Miframe,text= ",")
coma.grid(row=5,column=2)

numero0=Button(Miframe,text= 0)
numero0.grid(row=5,column=1)
numero1=Button(Miframe,text= 1)
numero1.grid(row=4,column=0)
numero2=Button(Miframe,text= 2)
numero2.grid(row=4,column=1)
numero3=Button(Miframe,text= 3)
numero3.grid(row=4,column=2)
numero4=Button(Miframe,text= 4)
numero4.grid(row=3,column=0)
numero5=Button(Miframe,text= 5)
numero5.grid(row=3,column=1)
numero6=Button(Miframe,text= 6)
numero6.grid(row=3,column=2)
numero7=Button(Miframe,text= 7)
numero7.grid(row=2,column=0)
numero8=Button(Miframe,text= "8")
numero8.grid(row=2,column=1)
numero9=Button(Miframe,text= "9")
numero9.grid(row=2,column=2)







raiz.mainloop()