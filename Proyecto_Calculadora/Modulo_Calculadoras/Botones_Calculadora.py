from tkinter import *
from Modulo_Calculadoras.Operaciones_calculadora import *
#contador=0


def contruir_botones(self,Botones,filas_botones,columnas_botones):
    contador=0
    for fila in range(1,filas_botones+1):
        for columna in range(columnas_botones):
            Botones[contador].grid(row=fila,column=columna)
            contador+=1

def colocar_boton(self,valor,mostrar=True,ancho=9,alto=1):
    return Button(self.ventana,text=valor,width=ancho, height=alto, font=("Helvetica",9),
                command=lambda:pulsaciones_teclas(self,valor,mostrar))