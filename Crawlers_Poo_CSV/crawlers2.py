from bs4 import BeautifulSoup 

miDoc =""" 

    <html>
        <style>
            .pImportante{
                color:red;
            }
        </style>
        <body>
        <p class='pImportante'> Este es el primer párrafo</p>
        <p> Este es el segundo párrafo</p>
        <a> Es un vinculo </a>
        </body>
    </html>



""" # la triple comilla es cuando quieres meter varias lineas

Almacenar = BeautifulSoup(miDoc,"html.parser")

for parrafo in Almacenar.find_all("p"): #find all es para que busque todos los parrafos en el documento

    print(parrafo.attrs) #atributos del css
    print(parrafo.text) #escribe el texto que se encuentra en cada p 


print(Almacenar)