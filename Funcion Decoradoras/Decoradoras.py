def funcion_decoradora(funcion_parametro):

    def funcion_interna(*args,**kwargs): # *args significa que recibe un numero indeterminado de parametros
                                         # **kwargs es para recibir una estructura clave-valor (ejemplo diccionario)

        print("voy a realizar la operacion: ")
        funcion_parametro(*args,**kwargs)
        print("ya tienes el calculo realizado")

    return funcion_interna




@funcion_decoradora
def suma(num1,num2,num3,num4):
    print(num1+num2+num3+num4)

@funcion_decoradora
def resta(num1,num2):
    print(num1-num2)

@funcion_decoradora
def potencia(base,exponente):

    print(pow(base,exponente)) #pow hace la potencia

suma(5,7,23,12)
resta(12,3)
potencia(base=5,exponente=3) #base es clave y valor es 5