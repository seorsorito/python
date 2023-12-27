import sys
intentos =0
def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplica(num1,num2):
    return num1*num2
def divide(num1,num2):
    try:
     return num1/num2
    except ZeroDivisionError:
        print("no se puede dividir entre 0")
        return "Operacion erronea"
while True:
    try:
        op1=(int(input("Introduce el primer numero: ")))

        op2=(int(input("Introduce el segundo numero: ")))
        break
    except ValueError:
        print("el valor introducido no es un numero")
        intentos=intentos+1
        if intentos ==3:
            print("has consumido todos los intentos")
            sys.exit()
operacion=input("Introduce la operacion a realizar: (suma,resta,multiplica,divide) ")

if operacion == "suma":
    print(suma(op1,op2))

elif operacion == "resta":
    print(resta(op1,op2))

elif operacion == "multiplica":
    print(multiplica(op1,op2))

elif operacion == "divide":
    print(divide(op1,op2))
else:
    print("operacion no válida")

print("Operación ejecutada, Continuación del programa")
