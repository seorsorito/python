def capitales_mundo(*ciudades):
    for capital in ciudades:
       # for letra_capital in capital: #este bucle for se mete dentro del primer bucle 
            yield from capital
        

capitales_devueltas=capitales_mundo("Berlin","Roma","Madrid","Pekín","Tokyo")

print(next(capitales_devueltas))