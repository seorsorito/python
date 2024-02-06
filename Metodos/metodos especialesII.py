class Persona():
   
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    #def __str__(self):
        #return "Datos de la persona \n " + "nombre: " + self.nombre+"\n apellido: " +self.apellido + "\n Edad: " + str(self.edad)
    def __repr__(self): #funciona igual que str pero es mas preciso que str
        return "Datos de la persona \n " + "nombre: " + self.nombre+"\n apellido: " +self.apellido + "\n Edad: " + str(self.edad)

p1=Persona("Victor","Gayo","24")

print(p1)
print("------------------------------")

import datetime

hoy=datetime.date.today()
print(str(hoy))
print(repr(hoy)) #identifica al objeto de forma inequívoca

print("-----------------------------")

class agenda():

    def __init__(self):
        
        self.miagenda={}

    def agregar_personas(self,nombre,telefono):
        self.miagenda[nombre]=telefono
    def __len__(self): #para objetos que no se pueden dar la longitud se sobreescribe
        return len(self.miagenda)

agendaPersonal=agenda()

agendaPersonal.agregar_personas("Juan","564675434")
agendaPersonal.agregar_personas("victor","564675434")
agendaPersonal.agregar_personas("maria","564675434")
agendaPersonal.agregar_personas("jesus","564675434")
agendaPersonal.agregar_personas("damiel","564675434")
agendaPersonal.agregar_personas("gertica","564675434")


print(len(agendaPersonal))
