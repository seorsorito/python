import queue 

#miCola =queue.Queue() #tipo F.I.F.O
#miCola =queue.LifoQueue() #tipo L.I.F.O
miCola =queue.PriorityQueue(3) #se indica el tamaño que debe tener, en caso de no especificar sera infinito



miCola.put((1,"Madrid")) #ASI SE REALIZA PARA PRIORITY
miCola.put((2,"Buenos Aires"))
miCola.put((3,"Pekin"))

#miCola.put("Pekin") ASI FUNCIONA CON LOS OTROS DOS ELEMENTOS

print(miCola.get())

print("A continuación se imprimen los elementos restantes en la cola")

for elemento in miCola.queue:
    print(elemento)