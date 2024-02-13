from io import open

archivo_externo=open("primerArchivo.txt","r+") #indica modo lectura y escritura

lista_archivo=archivo_externo.readlines()

lista_archivo[1]="Hoy es martes y empezamos la semana \n"

archivo_externo.seek(0)

archivo_externo.writelines(lista_archivo)

archivo_externo.close()

print(lista_archivo)