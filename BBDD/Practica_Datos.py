import sqlite3

miConexion= sqlite3.connect("BBDD/miBBDD")

miCursor = miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")#para poder crear las tablas
#UNA VEZ EJECUTADA LA TABLA TENEMOS QUE COMENTAR LA LINEA DADO QUE INTENTARA CREAR OTRA TABLA CON EL MISMO NOMBRE

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('Camiseta',25,'Moda')")

Muchosproductos=[

    ("Patin",100,"Deportes"),
    ("Cenicero",20,"Cerámica"),
    ("Pantalon",80,"Moda")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",Muchosproductos) #consulta parametrica

miConexion.commit() #cada vez que hagamos algo tenemos que confirmar esa acción con un commit

miCursor.close()
miConexion.close()