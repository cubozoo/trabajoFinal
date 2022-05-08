import mysql.connector

conexion = mysql.connector.connect(
    user = 'root',
    password= '',
    host= 'localhost',
    database='musicaUwU'
)
ejecutar = conexion.cursor()
query = "select * from usuarios"
ejecutar.execute(query)
