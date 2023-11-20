capitales={"China":"Pekín","India":"Nueva Dehli","Japon":"Tokio","Tailandia":"Bankog"}

for key in capitales:
    valor=capitales[key]
    print(key)
    print(valor)

print(capitales.items())

for key,valor in capitales.items():
    print(key + "-> "+valor)