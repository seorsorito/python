nombrePersonas= []
def agregar_a_lista(lista,nombreIntroducido):
    try:
        if nombreIntroducido in lista:
            raise ValueError
        else:
            lista.append(nombreIntroducido)
    except ValueError:
        print("Error. Este nombre ya se ha introducido ")

introducidos = 1

while introducidos<11:

    nombre=input("Introduce nombre: ")
    agregar_a_lista(nombrePersonas,nombre)
    introducidos+=1

print(nombrePersonas)