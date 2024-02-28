import sqlite3 

miConexion= sqlite3.connect("BBDD/GestionPedidos")

miCursor = miConexion.cursor()

miCursor.execute('''
    
    CREATE TABLE PRODUCTOS (
                 
        ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        NOMBRE_ARTICULO VARCHAR(40),UNIQUE,
        PRECIO INTEGER,
        SECCION VARCHAR(20)
                 )
                 
                 
                 
                 
                 
                 
                 ''')

misProductos=[

    ("camiseta",35,"Moda"),
    ("pantalon",17,"Moda"),
    ("coche",45,"jugueteria"),
    ("gorra",23,"Deportes")
]

#CON PRIMARY KEY INDICAMOS EL CAMPO CLAVE Y AUTOINCREMENT HACE QUE SE RELLENE SOLO
#CON UNIQUE HACE QUE NO SE PUEDA REPETIR TAMPOCO

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)",misProductos) #USAMOS NULL PARA EL CAMPO ID

miCursor.execute("INSERT INTO PRODUCTOS VALUES(NULL,'zapatilla',90,'Deportes')")

miConexion.commit()

miCursor.close()
miConexion.close()