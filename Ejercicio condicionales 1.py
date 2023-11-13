print("Decalaración de la renta")

renta=float(input("Cual es tu renta anual? "))

if renta<12000:
    print("Para "+str(renta)+" le corresponde un 7%")

elif renta>12000 and renta<18000:
    print("Para "+str(renta)+" le corresponde un 15%")

elif renta>18000 and renta<35000:
    print("Para "+str(renta)+" le corresponde un 21%")

elif renta>35000 and renta<70000:
    print("Para "+str(renta)+" le corresponde un 35%")

else:
    print("Para "+str(renta)+" le corresponde un 45%")