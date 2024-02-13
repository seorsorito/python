from io import open

#archivo_externo=open("primerArchivo.txt","w") con esto empezamos la primera frase 

#archivo_externo=open("primerArchivo.txt","a") #con w se agrega texto al archivo nuevo. con a se agrega aalgo a un archivo ya existente (append)

archivo_externo=open("primerArchivo.txt","r") #asi es para leer un archivo externo 

#archivo_externo.write("\n manipulamos en documento")

informacion = archivo_externo.read()

#lineas=archivo_externo.readline() #esta solo lee la primera linea que se encuentra

lineas=archivo_externo.readlines()

#archivo_externo.close() #cerramos el flujo de datos

print(informacion)

archivo_externo.seek(0) #para poner el cursor donde quieras dado que una vez finalizado el cursor se encuentra al final
#podemos desde el read hacer lo mismo pero se relaliza el efecto contrario
print(informacion)

#for imprimir in lineas:
    #if len(imprimir) != 0:
        #print(imprimir)
