class Persona():
   
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
    def __str__(self):
        return "Datos de la persona \n " + "nombre: " + self.nombre+"\n apellido: " +self.apellido + "\n Edad: " + str(self.edad)

p1=Persona("Victor","Gayo","24")

print(p1)

print("..............................................")

class Alumno():

    almacen_datos =[]

    def __init__(self,*datos): #para meter un numero x de datos se utiliza una tupla

        for dato in datos:

            self.almacen_datos.append(dato)
    def __str__(self):
        return "Datos del alumno \n " + "nombre: " + str(self.almacen_datos[3])+"\n apellido: " +str(self.almacen_datos[1]) + "\n Edad: " + str(self.almacen_datos[2])

c1=Alumno("Victor","Gayo",24,18000,"Accenture")#no importa el número de parámetros que le pase, se almacenan todos en la tupla y no me da error
print(c1)

print("-------------------------------------------------")

class trabajador():
     
     almacen_trabajo=[]

     def __init__(self,*datos2): 

        for dato1 in datos2:

            self.almacen_trabajo.append(dato1)
        
        self.getDatos(self.almacen_trabajo)
    
     def getDatos(self,info):
         
         for dato1 in info:
             print(dato1)
    
        
b1=trabajador("Victor","Gayo",24,18000,"Accenture")
print(b1)   

print(".............................................")

class Diccionario():

    almacen_registro=[]

    def __init__(self,**registro): #con el ** se convierte en un diccionario
        
        elementos =registro.items()
        for clave,valor in elementos:
            print(clave,"",valor)

d1=Diccionario(Nombre="Juan",Apellido="Diaz",Edad=23)
        
