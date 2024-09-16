import mysql.connector
from mysql.connector import Error

def connection():
    try:
        connection=mysql.connector.connect(
            user="root",
            password="",
            host="localhost",
            database="user"
        )
        if connection.is_connected():
            print("connection sucuessfull")
            return connection
    
    except Error as e:
        print(f"there is error:{e}")
