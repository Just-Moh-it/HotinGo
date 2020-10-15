import tkinter as tk
import mysql.connector

# SQL Connectivity

connection=mysql.connector.connect(host="remotemysql.com", 
                            user="OupAGhC9dM", 
                            password="KYVO7iezPw", 
                            database = "OupAGhC9dM", 
                            port="3306", 
                            charset="utf8", autocommit=True)
cursor=connection.cursor()


cursor.execute("select * from login;")
print(cursor.fetchall())


# Tkinter

