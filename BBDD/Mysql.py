import mysql.connector

MiConexion=mysql.connector.connect(host="localhost",database="base_datos",user="root",password="1234")

Micursor=MiConexion.cursor()

Micursor.execute("INSERT INTO ALUMNOS VALUES(6,'Juan','Davila','cesur',7,34)")

MiConexion.commit()


Micursor.close()
MiConexion.close()