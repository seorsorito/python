#edad=int(input("Introduce tu edad, por favor: "))

#while edad <18 or edad>100:
    #print("Lo lamento no es válida")
    #edad=int(input("Introduce tu edad, por favor: "))

#print("Gracias puedes pasar")
#print("Tu edad es "+ str(edad))
import math
print("Programa para hallar la raíz cuadrada de un valor numérico")

numero=int(input("Introduce un número: "))
intentos=1 #es una variable contador para guardar el numero de intentos

while numero<0:
    print("El valor numérico no puede ser negativo")
    numero=int(input("Introduce un número: "))
    intentos=intentos+1

    if intentos==3:
        
        break #utilizamos break para salir del bucle de forma forzosa

if intentos==3:
   print("Intentalo más tarde")
else:
    print(math.isqrt(numero))

 





