print("Obtención becas alumnos 2023")

nota_media=int(input("Introduce tu nota media "))
hermanos_en_centro=int(input("Introduce numero de hermanos ")) 
distancia_al_centro=int(input("Introduce distancia al centro "))
renta_familiar=int(input("Introduce renta familiar "))

if nota_media>7 or hermanos_en_centro>3 or (distancia_al_centro>20 and renta_familiar< 20000):
    print("Se te concede la beca")
else:
    print("Lo lamentamos, pero no te la concedemos")