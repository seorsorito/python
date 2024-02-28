import sqlite3 

miConexion= sqlite3.connect("BBDD/miBBDD")

miCursor = miConexion.cursor()


miCursor.execute("SELECT * FROM PRODUCTOS")


Productos=miCursor.fetchall() #convierte los registros en una lista almacenada en Productos


#miConexion.commit() no se requiere al leer
 

for p in Productos:
    print("nombre: ", p[0], " precio: ",p[1])


miCursor.close()
miConexion.close()