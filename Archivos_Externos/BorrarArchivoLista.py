import io 
import os 

lista_archivos = os.listdir("./")

for archivo in lista_archivos:

    if archivo == "tirar.py":

        os.remove(archivo)