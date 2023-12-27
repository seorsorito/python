print("Números primos")
primer=int(input("Dame un numero: "))
segundo=int(input("Dame un segundo número: "))

def es_primo (numero):
    for n in range(2,numero):
        if numero % n == 0:
            return False
    print(str(numero)+" es primo")
    return True

for i in range(primer,segundo):
    es_primo(i)
