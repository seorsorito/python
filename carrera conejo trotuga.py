animal1="conejo"
animal2="tortuga"
carrera=1
carrera2=1
while carrera!=11:
    print(animal1+ " va en la posición "+ str(carrera)+ " de la carrera")  
    carrera=carrera+1
    if carrera%5==0:
        print(animal2+ " va en la posición "+ str(carrera2)+ " de la carrera")
        carrera2=carrera2+1
