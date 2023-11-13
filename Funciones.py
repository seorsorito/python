def imprimeMensaje(): #definición de una función
    print("Estoy con python")
    print("tengo "+ str(23) + "años")
    print("Solo hago print "+ str(True))

imprimeMensaje() #invocación de una función 

def funcionesquedevuelven():
    return "Esto es lo que devuelve"

devuelto = funcionesquedevuelven()

print(devuelto)

def mensaje_personalizado(mensaje,valor1,valor2): #mensaje es un parámetro o argumento que solo se define en la función
    return mensaje + str(valor1+valor2)+" Y encima concateno"

print(mensaje_personalizado("Aprendiendo a programar con ",16,7)) #aqui hemos definido ese parametro 
#print(mensaje_personalizado("Aprendiendo a progrmaar")) esto sería para verlo en consola

