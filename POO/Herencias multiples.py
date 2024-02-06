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
        persona.__init__(self,nombre,apellido,edad) #mismo caso que el de trabajador
        self.escuela=escuela
    
    def estudiar(self):
        return "Estoy estudiando"
    
    def getDatosPersonales(self): #getter
        return super().getDatosPersonales()+ " Escuela: " + self.escuela #para poder meter el método escuela dentro de datos personales pero solo en esta clase


class trabajador(persona):
    def __init__(self, nombre, apellido, edad,empresa):
        persona.__init__(self,nombre, apellido, edad)#no se pone super para que pueda funcionar la herencia multiple, además se pone un self
        self.empresa=empresa

    def getDatosPersonales(self):
        return super().getDatosPersonales()+ " Empresa: " + self.empresa
    
    def trabaja(self):
        return "Estoy trabajando"

class Director (trabajador,estudiante): #el orden de la herencia importa en este caso trabajdor tiene preferencia a estudiante
    def __init__(self, nombre, apellido, edad, empresa,escuela,bonus):
        trabajador.__init__(self,nombre, apellido, edad, empresa) #en este caso la clase padre son trabajador y estudiante, no persona !
        estudiante.__init__(self,nombre, apellido, edad, escuela) #en este caso la clase padre son trabajador y estudiante, no persona !
        self.bonus=bonus
    def getDatosPersonales(self):
        return super().getDatosPersonales()+ " Bonus: " + str(self.bonus)
    
    def dirige(self):
        return "Estoy dirigiendo"
    


persona1=persona("Juan","gomez",35)

estudiante1=estudiante("Carlos","Alvarez",23,"Fortuny")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
print("-----------------------------------------")

trabajador1=trabajador("Victor","Gayo",24,"Ardanuy")
print(trabajador1.getDatosPersonales())

Director1=Director("Jose","Diaz",45,"typsa","cesur",200)
print(Director1.getDatosPersonales())
