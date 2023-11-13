def evaluarAlumno(nota):
    valoracion="desconocida"
    if nota < 5:
        valoracion= "suspenso"
    elif nota > 10: #se pone un elif cuando quieres que el else actue con varios if
        valoracion="Nota incorrecta"
    else:
        valoracion="aprobado"
    return valoracion 

notaalumno=int(input("Introduce tu nota: ")) #se le aplica un input para introducir por consola el dato

print(evaluarAlumno(notaalumno))                         

