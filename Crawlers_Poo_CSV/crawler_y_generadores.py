from bs4 import BeautifulSoup 
import requests
from urllib.parse import urljoin #para rutas absolutas en imagenes
import time
import csv



class PostCrawler():

    def __init__(self,titulo,emoticono,contenido,imagen) :
        self.titulo=titulo
        self.emoticono=emoticono
        self.contenido=contenido 
        self.imagen=imagen

class Extractor():

    def ExtraeInfo (self):

        urlBase = "https://python.beispiel.programmierenlernen.io/"
        

        while urlBase!="":

            miDoc =requests.get(urlBase)
        
            Almacenar = BeautifulSoup(miDoc.text,"html.parser")

            time.sleep(2)#metemos el metodo sleep para no cargar el servidor de peticiones y ralentizar el código

            for card in Almacenar.select(".card"):
                titulo = card.select(".card-title span")[1].text
                emoticono= card.select_one(".emoji").text
                contenido =card.select_one(".card-text").text
                imagen=urljoin(urlBase,card.select_one("img").attrs["src"])#gracias a urljoin tengo la ruta absoluta de las imagenes

                yield PostCrawler(titulo,emoticono,contenido,imagen) #GENERADOR
            
            boton_siguiente=Almacenar.select_one(".navigation .btn")
            if boton_siguiente:
                paginas = urljoin(urlBase,Almacenar.select_one(".navigation .btn").attrs["href"]) #sacamos la ruta del boton para la pagina 2
                urlBase=paginas #esto hace que el request dentro del bucle realize las peticiones dentro de la pagina 2
                print(paginas)
            else:
                urlBase=""#metemos la instrucion para salir del bucle while despues de llegar a la ultima pagina y poder llegar al return
            
        return 


Primerposts = Extractor()
listaPosts = Primerposts.ExtraeInfo()
print(listaPosts)


contador = 0

for caracteristicas in listaPosts:

    if contador==12:
        break 
    contador+=1 #por el contador solo se hara la peticion de los 12 primeros sin tener que consumir recursos en exceso gracias al generador

    print(caracteristicas.emoticono)
    print(caracteristicas.titulo)
    print(caracteristicas.contenido)
    print(caracteristicas.imagen)
    print()

"""with open('posts.csv', 'w', newline='',encoding='utf-8') as csvfile: #con esto creamos un archivo csv para almacenar los datos que sacamos de la pagina
    postwriter = csv.writer(csvfile, delimiter=';',#ponemos ; porque excel cada limitador con ; lo pone en una columna
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for mipost in Primerposts.ExtraeInfo():
        postwriter.writerow([mipost.emoticono,mipost.titulo,mipost.contenido,mipost.imagen])"""
    
    
    
 


