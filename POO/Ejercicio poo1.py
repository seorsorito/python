class CuentaCorriente():
    Titular=""
    Ncuenta=0
    saldo=0

    def __init__(self,Titular,Ncuenta,saldo):
        self.Titular=Titular 
        self.Ncuenta=Ncuenta 
        self.saldo=saldo 
    def getdatos(self):
        return "El titular de la cuenta es " + self.Titular + " el numero de cuenta es " + str(self.Ncuenta) +\
        " el saldo es " + str(self.saldo)
    def ingresar(self):
        pregunta=input("quieres ingresar? ")
        if pregunta =="si":
            ingreso=int(input("Cuanto quieres ingresar? "))
            self.saldo=self.saldo+ingreso
        else:
            pass
    def retirar(self):
        pregunta2=input("quieres retirar? ")
        if pregunta2=="si":
            retiro=int(input("Cuanto quieres retirar? "))
            self.saldo=self.saldo+retiro
        else:
            pass

p1=CuentaCorriente("Victor",67455645,11000)
p1.ingresar()
p1.retirar()
print(p1.getdatos())


