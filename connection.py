import mysql.connector

connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpw",
        database="schooldb"
    )
