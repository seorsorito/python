frases_ordenar = ["Los lunes son los mejores dias para programar", "Python es moderno","Veremos Inteligencia Artificial mas adelante","Lambda simplifica el codigo"]

"""def ordena_frases(o):

    return len(o.split())

frases_ordenar.sort(key=ordena_frases,reverse=True)"""

#print(frases_ordenar)


frases_ordenar.sort(key=lambda o: len(o.split()),reverse=True)
print(frases_ordenar)