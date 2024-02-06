class persona():

    def hablar(self):
        return "Hablo como una persona"
    
class trabajador(persona):

    def hablar(self):
        return "Hablo como un trabajador" #sobreescritura
    
class director(trabajador):

    def hablar(self):
        return "Hablo como un director" 
    
def hazleshablar(listasdelasPersonas):
    for persona in listasdelasPersonas:
        print(persona.hablar())
Antonio=persona()
Maria=trabajador()
Ana=director()

print(Antonio.hablar())
print(Maria.hablar())
print(Ana.hablar())
print("-------------------------")

listaPersonas= [Antonio,Ana,Maria]

hazleshablar(listaPersonas)