import Ejerciciopoo1

class CuentaJoven (Ejerciciopoo1.CuentaCorriente):
    def __init__(self, Titular, Ncuenta, saldo):
        super().__init__(Titular, Ncuenta, saldo)
        
        

    def getBonus(self):
         pregunta4=input("Tienes un bonus? ")
         if pregunta4 =="si":
            bonus_promocion=int(input("De cuánto es el bonus? "))
            self.saldo=self.saldo+bonus_promocion
         else:
            pass
    
    def getdatos(self):
        return super().getdatos() + "Bonus: " + (self.getBonus)
    def ingresar(self):
        return super().ingresar()
    def retirar(self):
        return super().retirar() 
    
c1=CuentaJoven("Victor",67455645,11000)
c1.getBonus()
print(c1.getdatos())
