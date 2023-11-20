nombre = "Victor gayo"
contador=0

for i in nombre:
    if i == " ":
        continue
    
    contador+=1  

print(contador)

profesion = "delineante" 

cuenta=0 

for i in profesion:
    if i == "o":
        pass 
    contador +1 

print(cuenta)

email =input("Intorduce tu email: ")
for i in email:
    if i =="@":
        arroba=True 
        break 
else:
    arroba=False
print(arroba)