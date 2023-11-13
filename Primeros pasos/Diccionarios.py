Capitalesdelmundo={"España":"Madrid","Alemania":"Berlín","Belgica":"Bruselas","Francia":"Paris"}

Capitalesdelmundo["Italia"]="Roma" #para agregar un nuevo valor al diccionario
Capitalesdelmundo["España"]="Elmundo"#para cambiar un valor del diccionario
del Capitalesdelmundo["Francia"] #Para eliminar un elemento del diccionario
print(Capitalesdelmundo)

Datos={"España":"Madrid",23:"M.Jordan",True:"Verdad"}

print(Datos)

Clavecapitales=["España","Reino Unido","Colombia","Argentina"]

Clavemundo={Clavecapitales[0]:{"Madrid":["Chamberi","Alamagro","Sol","Gran via"]},Clavecapitales[1]:"Londres",Clavecapitales[2]:"Bogota",Clavecapitales[3]:"Buenos Aires"} 
#En madrid he metido otro diccionario con una tupla apra definir sitios de Madrid
print(Clavemundo)
print(Clavemundo["Argentina"])
print(Clavemundo.keys()) #para imprimir todos las claves del diccionario
print(Clavemundo.values()) #Para imprimir todos los valores del diccionario
print(len(Clavemundo))