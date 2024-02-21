import re 

lista_nombres = ["Antonio Banderas","Salma Hayek","Tomas Roncero","Antonio Resines","Friedrich Hayek"]

lista_dominios = ["http://www.pilforasinformaticas.es","ftp://www.pilforasinformaticas.es","http://www.pilforasinformaticas.com","ftp://www.pilforasinformaticas.com"]

lista_terminos = ["camión","camion","niños","niñas","ejemplo"]

Codigo_productos = ["Ma1","Se1","Ma2","Va:1","Ba1","Se2","Ma.3","Ma4","SeA","SeD","Va2","SeC"]

for nombre in lista_nombres:
    if re.findall("^Antonio",nombre): #todos los que comiencen por "antonio" para eso sirve el ^
        print(nombre) 


for nombre in lista_nombres:
    if re.findall("Hayek$",nombre): #todos los que acaben por "Hayek" para eso sirve el $
        print(nombre) 


for dominios in lista_dominios:
    if re.findall("^http",dominios): 
        print(dominios) 

for terminos in lista_terminos:
    if re.findall("cami[oó]n",terminos): # el [] nos sirve para poder realizar busquedas de la misma palabra pero con diferencias de acentuacion
        print(terminos) 

for terminos in lista_terminos:
    if re.findall("niñ[oa]s",terminos): # el [] nos sirve para poder realizar busquedas de la misma palabra pero con diferencias de genero tambien
        print(terminos) 

for terminos in lista_terminos:
    if re.findall("[p-z]",terminos): # el [] nos devuelve todos los terminos que en el interior tengan una letra entre el rango establecido
        print(terminos)

for terminos in lista_terminos:
    if re.findall("^[a-f]",terminos): # el [] nos devuelve todos los terminos que empiezan con una letra entre el rango establecido
        print(terminos)

for codigos in Codigo_productos:
    if re.findall("Ma[^1-3]",codigos): # por el ^ hace lo contrario y busca los que no tengan ese numero pero si el Ma
        print(codigos)

for codigos in Codigo_productos:
    if re.findall("Se[^3^C]",codigos): # para poner varias condiciones 
        print(codigos)

for codigos in Codigo_productos:
    if re.findall("[.:]",codigos): # para poner varias condiciones 
        print(codigos)