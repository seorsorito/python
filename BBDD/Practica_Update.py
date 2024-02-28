import sqlite3 

miConexion= sqlite3.connect("BBDD/GestionPedidos")

miCursor = miConexion.cursor()

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=63 WHERE ID=4")

miCursor.execute("DELETE FROM PRODUCTOS  WHERE ID=3")



miConexion.commit()

miCursor.close()
miConexion.close()