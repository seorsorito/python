def comparalistas(lista1,lista2):
    if lista1 != lista2:
        return False
    else:
        for i in range(0,len(lista1)):
            if lista1[i]!=lista2[i]:
                return False
    
    return True
            

alumnosA="Juan","Jose","Paco","Epe"
alumnosB="Juan","Jose","Paco","Eape"

print(comparalistas(alumnosA,alumnosB))