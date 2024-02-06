usuario = input("introduce tu usuario: ")

print("El usuario introducido es: ",usuario.upper()) #los metodos siempre con ()
print("El usuario introducido es: "+ usuario.capitalize())

edad=input("Introduce tu edad: ")
while(edad.isdigit()==False): #esto se utiliza para que no me quede en error cuando se escribe algo que no sea un numero
    print("El valor no es correcto")
    edad=input("Introduce tu edad: ")

if int(edad)<18:
    print("no puedes pasar")

else:

    print("puedes pasar")

