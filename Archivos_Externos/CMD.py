import os 
from io import open

#os.makedirs("PruebaDirectorio2") #se crea donde estamos trabajando

os.chdir("PruebaDirectorio2") #para moverme dentro de esa carpeta

#archivo_externo=open("Archivocmd2.docx","w")

#archivo_externo.write("metemos un documento dentro de la carpeta creada en cmd")

#archivo_externo.close()

#os.rename("Archivocmd.txt","NombreCambiado.txt") #para cambiar el nombre de un archivo

os.remove("Archivocmd2.docx") #para eliminar archivos

os.chdir("../") #para ir una carpeta arriba

os.rmdir("PruebaDirectorio2") #no se puede eliminar una carpeta sin borrar todos los archivos que contenga

#print(os.getcwd()) #para saber la ruta donde se encuentra

#print(os.listdir("./")) # con esto nos da una lista de lo que se encuentra dentro del directorio