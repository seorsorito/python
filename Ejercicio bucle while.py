import random
numero=random.randint(1,100)
usuario=int(input("Introduce un numero entre el 1 y 100: "))
contador=1
intentos=1
while usuario<1 or usuario>100:
    print("Ese numero no es válido")
    usuario=int(input("Introduce un numero entre el 1 y 100: "))
    contador=contador+1
    if contador==4:
        break
if contador==4:
    print("Te quedas sin jugar")
else:
    while usuario!=numero:
        if (usuario<numero):
            print("Tu numero es menor")     
        if (usuario>numero):
            print("Tu numero es mayor")
            
    
        usuario=int(input("Introduce un numero entre el 1 y 100: "))
        intentos=intentos+1

            
    print("Enhorabuena ese era el número y el numero de intentos es "+str(intentos))
            
            
        



