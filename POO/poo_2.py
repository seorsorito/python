class Persona():
    __nombre=""
    apellido=""
    __edad=0
    genero="sin definir"

    def __init__(self,nombre,apellido,genero): #contructor 
        self.__nombre=nombre
        self.apellido=apellido
        self.genero=genero
    
    def setEdad(self,Años): #setter

        if Años < 0 or Años > 100:
            print( "Error en la edad")
        else:
            self.__edad=Años
            return self.__edad

    def habla(self):
        return "la persona que se llama "+ self.__nombre + " esta hablando"
    
    def camina(self):
        return "la persona que se llama "+ self.__nombre + " esta caminando"
    def getdatos(self):
        return "nombre: "+ self.__nombre+ " Apellido: "+ self.apellido +\
        " Edad: "+ str(self.__edad)+ " Género: "+ self.genero #el \ es para poder seguir el codigo debajo

p1=Persona("Victor","Gayo",24,"masculino") #le damos las propiedades al constructor

p1.setEdad(53)

print(p1.getdatos())
