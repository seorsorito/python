class persona():
    
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    
    def getDatosPersonales(self): #getter
        return "Nombre: " + self.nombre + " Apellido: "+ self.apellido + " Edad: " + str(self.edad)
    
    def habla(self):
        return "Estoy hablando"
    def piensa(self):
        return "Estoy pensando"
    def camina(self):
        return "Estoy caminando"
    def come(self):
        return "Estoy comiendo" 
    
class estudiante(persona): #al meter la clase persona en el paréntesis ya hereda de esa clase
    def __init__(self,nombre,apellido,edad,escuela):
        super().__init__(nombre,apellido,edad) #para llamar al constructor de la clase padre
        self.escuela=escuela
    
    def estudiar(self):
        return "Estoy estudiando"
    
    def getDatosPersonales(self): #getter
        return super().getDatosPersonales()+ " Escuela: " + self.escuela #para poder meter el método escuela dentro de datos personales pero solo en esta clase


persona1=persona("Juan","gomez",35)

estudiante1=estudiante("Carlos","Alvarez",23,"Fortuny")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
