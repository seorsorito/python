sistema_solar = "Mercurio Venus Tierra Marte Jupiter Saturno Urano Neptuno Pluton Tierra Venus" #si estan repetidos no los cuenta

planetas=set()

for planeta in sistema_solar.split(" "): #con el metodo split sabe distinguir cada elemento por el espacio en blanco pero se indica con lo que quieres separar
    planetas.add(planeta)

print(planetas)
print(len(planetas))