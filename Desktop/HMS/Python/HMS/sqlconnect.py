import mysql.connector
from tkinter import messagebox

# ===================SQL Connectivity=================

# SQL Connection
connection=mysql.connector.connect(host="remotemysql.com", 
                            user="OupAGhC9dM", 
                            password="KYVO7iezPw", 
                            database = "OupAGhC9dM", 
                            port="3306", 
                            charset="utf8", autocommit=True)
cursor=connection.cursor()

# SQL functions

def checkUser(username, password):
    cmd="Select count(username) from login where username='"+username+"' and password='"+password+"';"
    cursor.execute(cmd)
    print(cmd)
    return cursor.fetchone()[0]>=1

