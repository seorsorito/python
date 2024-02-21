import re 

cadena = "Estoy realizando trabajos con regex hoy entre semana y antes de examenes. Los examenes son examenes dificiles para gente que no realiza muchos examenes"

busqueda = "examenes"
#print(re.search("examenes",cadena))

texto_encontrado=re.search(busqueda,cadena)

if re.search(busqueda,cadena) is not None:

    print("Se encontro el término " + busqueda  + " en "+ str(texto_encontrado.start())) #posicion del caracter con el cual empieza
    print("Se encontro el término " + busqueda  + " en "+ str(texto_encontrado.end())) #posicion del caracter con el cual termina
    print("Se encontro el término " + busqueda  + " en "+ str(texto_encontrado.span())) #tupla con ambas posiciones

else: 

    print("no se encontro el término" + busqueda)

print(re.findall(busqueda,cadena))

print(len(re.findall(busqueda,cadena)))