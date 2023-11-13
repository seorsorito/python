print("Obtencion del carnet de conducir")

edad=int(input("Introduce tu edad, por favor: "))
vision=input("Tienes la vision correcta?")

#if 18<edad<90:         esto funcionaria sin problema
 #print("Puedes presentarte a las pruebas")
if edad>=18 and edad<=90 and vision=="si":
 print("Puedes presentarte a las pruebas")
 
else:
 print("Lo siento, no cumples con la edad necesaria")


