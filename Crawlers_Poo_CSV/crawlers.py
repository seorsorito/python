import requests #es necesario tener requests instalado

mireq= requests.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")

print(mireq.status_code) #nos tiene que devolver un 200 para verificar que tenemos el documento hmtl

print(mireq.headers) #con este comando nos da informacion de un documento web 

print(mireq.text) #imprime todo el texto