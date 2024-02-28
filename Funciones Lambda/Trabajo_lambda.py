
"""def area_triangulo(base,altura):
    return (base * altura) /2 

triangulo1= area_triangulo(4,7)

triangulo2= area_triangulo(3,9) """


area_triangulo = lambda base,altura:(base*altura)/2

print(area_triangulo(3,4))


potencia_numero = lambda base,potencia: base ** potencia #eleva a una potencia

print(potencia_numero(2,3))

comision_formato= lambda comision: "¡{}$!".format(comision)

comision_Antonio=5700

print(comision_formato(comision_Antonio))

"""mi_lista = [(11,5),(12,23),(34,45),(2,78),(98,23)]

def ordena_lista(t):
    return t[0]+ t[1]


mi_lista.sort(key=ordena_lista) #para ordenar una lista

print(mi_lista)"""

mi_lista = [(11,5),(12,23),(34,45),(2,78),(98,23)]


mi_lista.sort(key=lambda t: t[0]+t[1]) #para ordenar una lista

print(mi_lista)

musicos = ["Paul McCartney","Bruce Springsteen","Tina Turner","Justin Bieber","Elton John"]

def ordena_musicos(m):
    return m.split()[1]

musicos.sort(key=ordena_musicos)

print(musicos)