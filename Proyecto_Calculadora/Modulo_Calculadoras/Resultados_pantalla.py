from tkinter import *


def mostrar_pantalla(self,valor):
    self.Pantalla.insert(END,valor)
def borrar_pantalla(self):
    self.Pantalla.delete(0,END) #se le da dos parametros porque puede borrar ciertas partes unicamente
