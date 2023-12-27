Paises = {}
Pais=input("Introduce el pais: ")

while Pais != "salir":
    ciudad =input("Introduce la ciudad: ")
    lista_ciudades=Paises.setdefault(Pais,[ciudad])
    if lista_ciudades!=[ciudad]:
        Paises[Pais].append(ciudad)
    
    Pais=input("Introduce el pais: ")

print(Paises)