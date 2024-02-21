import re 

nombre1="Lara López" 

nombre2= "Jara Díaz"

nombre3= "Sandra Martín"

codigo1 = "gksfgwksfsdjvsfors255cvdsfglsdvmsdfs"

codigo2 = "fndsfs255zdjkcvsdjfsfdsfkwelr"

codigo3= "faifs133ndkfesfdfklgkl"


#la funcion match solo busca al principio, search busca en todo el string
#ignorecase es para ignorar las mayusculas y minisculas
if re.match("sandra",nombre3,re.IGNORECASE): #primero lo que buscas y luego donde y solo busca en el principio
    print("He encontrado la persona") 

else:
    print("No esta esa persona")

if re.match(".ara",nombre1,re.IGNORECASE): #donde se ubica el punto puede haber cualquier cosa
    print("He encontrado la persona") 

else:
    print("No esta esa persona")

if re.search("díaz",nombre2,re.IGNORECASE): #donde se ubica el punto puede haber cualquier cosa
    print("He encontrado la persona") 

else:
    print("No esta esa persona")

if re.search("255",codigo1): 
    print("He encontrado el codigo") 

else:
    print("No esta ese codigo")