from bs4 import BeautifulSoup 
import requests

miDoc =requests.get("https://python.beispiel.programmierenlernen.io/")


Almacenar = BeautifulSoup(miDoc.text,"html.parser")

iconos = Almacenar.select(".emoji")
titulo = Almacenar.select(".card-title span") #asi indicas que quieres acceder a spam dentro de card title

for texto in Almacenar.select(".card-text"):
    print(texto.text) 
    print("")

for imagen in Almacenar.select(".card-block img"):
    print(imagen.attrs["src"]) 
    print("")



print(iconos[0].text) #asi imprimimos solo el emoji
print(titulo[1].text)
