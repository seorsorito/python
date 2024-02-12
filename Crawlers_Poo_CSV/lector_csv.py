import csv 

with open('posts.csv', 'r', newline='',encoding='utf-8') as csvfile: #con esto leemos un archivo csv
    postreader = csv.reader(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for fila in postreader:
        print(', '.join(fila)) #forma de imprimir en consola el archivo csv