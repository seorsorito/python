class Coche():
    ruedas=4
    largoChasis=260 
    anchochasis=130
    arrancado=False

    def arrancar(self):
        #pass #se utiliza para que no de error el programa aunque no haga nada porque no puede haber metodos vacios
        self.arrancado=True
    
    def estadoCoche(self):
        if self.arrancado==True:
            return "El coche esta funcionado" 
        else:
            return "El coche esta parado"

Porche=Coche() #instanciamos para meter Porche en la clase coche //ejemplar de clase
Renault=Coche() #tienen las mismas propiedades y comportamientos // cada uno de ellos son objetos

print(Porche.anchochasis)
print("Tu coche tiene "+str(Renault.ruedas)+" ruedas")

Renault.arrancar() #hemos ejecutado el comportamiento del objeto
print(Renault.estadoCoche())
print(Porche.estadoCoche())

