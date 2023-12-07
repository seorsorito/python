def generalPares(limite):

    num=1 
 

    while num<limite:

        yield num*2 
        num=num+1
    
    
sucesionPares=generalPares(6)
for i in sucesionPares:
    print(i)