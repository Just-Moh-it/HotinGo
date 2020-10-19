import mysql.connector

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

def checkUser(username, password=None):
    cmd="Select count(username) from login where username='"+username.lower()+(("' and BINARY password='"+password) if password is not None else "")+"';"
    cursor.execute(cmd)
    print(cmd)
    cmd=None
    return cursor.fetchone()[0]>=1

def addUser(name, username, password, sec_que, sec_ans):
    cmd=f"Insert into login (name, username, password, sec_que, sec_ans) values ('{name}', '{username}', '{password}', '{sec_que}', '{sec_ans}');"
    cursor.execute(cmd)
    cmd=f"select count(name) from login where name='{name}' and username='{username}' and password='{password}' and sec_que='{sec_que}' and sec_ans='{sec_ans}'"
    cursor.execute(cmd)
    cmd=None
    return cursor.fetchone()[0]>=1