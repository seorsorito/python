import csv
with open('Ejemplo.csv', newline='') as csvfile:
    miCSV = csv.reader(csvfile, delimiter=';', quotechar='|')
    for linea in miCSV:
        print('- '.join(linea))