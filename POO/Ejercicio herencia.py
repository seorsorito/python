class vehiculo():
    color=""
    ruedas=0
    peso=0
    ancho=0
    alto=0

    def __init__(self,color,ruedas,peso,ancho,alto):
        self.color=color
        self.ruedas=ruedas
        self.peso=peso
        self.ancho=ancho
        self.alto=alto
    
    def getDatos(self):

        "El color es "+ self.color +"Tiene "+ self.ruedas+ " ruedas"+ "El peso es " + self.peso + "El ancho es " + self.ancho + "El alto es " + self.alto
    
    def Arrancar(self):
        return "Estoy en marcha"
    def Frenar(self):
        return "Estoy frenando"
    def Girar(self):
        return "Puedo girar"

class furgoneta(vehiculo):
    def __init__(self, color, ruedas, peso, ancho, alto,cilindrada,marchas,asientos,aireacondicionado):
        super().__init__(color, ruedas, peso, ancho, alto)
        self.cilindrada=cilindrada
        self.marchas=marchas
        self.asientos=asientos
        self.aireacondicionado=aireacondicionado 
    
    def Acelerar(self):
        return "Puedo acelerar"
    def Cargar(self):
        return "Carga lo que necesites"
    def Marchaatras(self):
        return "Voy marcha atras"
class coche(furgoneta):
    def __init__(self, color, ruedas, peso, ancho, alto, cilindrada, marchas, asientos, aireacondicionado):
        super().__init__(color, ruedas, peso, ancho, alto, cilindrada, marchas, asientos, aireacondicionado)

class moto(vehiculo):
    def __init__(self, color, ruedas, peso, ancho, alto,cilindrada, marchas, asientos):
        super().__init__(color, ruedas, peso, ancho, alto)
        self.cilindrada=cilindrada
        self.marchas=marchas
        self.asientos=asientos
    
    def Acelerar(self):
        return "Puedo acelerar"
    def Marchaatras(self):
        return "Voy marcha atras"
    def Derrapar(self):
        return "Puedo derrapar"
    def Saltar(self):
        return "Se puede saltar conmigo"
class bicicleta(moto):
    def __init__(self, color, ruedas, peso, ancho, alto, cilindrada, marchas, asientos):
        super().__init__(color, ruedas, peso, ancho, alto, cilindrada, marchas, asientos)
    
    

    
