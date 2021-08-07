import mysql.connector
import os

# Configurations
from config import config
from dotenv import load_dotenv

load_dotenv() # Imports environemnt variables from the '.env' file

# ===================SQL Connectivity=================

# SQL Connection
connection=mysql.connector.connect(host=config.get('DB_HOST'), 
                            user=os.getenv('DB_USER'), 
                            password=os.getenv('DB_PASSWORD'), 
                            database = config.get('DB_NAME'), 
                            port="3306", autocommit=config.get('DB_AUTOCOMMIT'))

cursor=connection.cursor()

# SQL functions

def checkUser(username, password=None):
    cmd="Select count(username) from login where username='"+username.lower()+(("' and BINARY password='"+password) if password is not None else "")+"';"
    cursor.execute(cmd)
    print(cmd)
    cmd=None
    return cursor.fetchone()[0]>=1

def addUser(username, password, sec_que, sec_ans):
    cmd=f"Insert into login (username, password, sec_que, sec_ans) values ('{username}', '{password}', '{sec_que}', '{sec_ans}');"
    cursor.execute(cmd)
    cmd=f"select count(name) from login where username='{username}' and password='{password}' and sec_que='{sec_que}' and sec_ans='{sec_ans}'"
    cursor.execute(cmd)
    cmd=None
    return cursor.fetchone()[0]>=1

def availableRooms():
    cursor.execute("select count(room_id) from rooms where currently_booked='0';")
    return cursor.fetchone()[0]


#============Python Functions==========

def acceptable(*args, acceptables):
    '''
        If the characters in StringVars passed as arguments are in acceptables return True, else returns False
    '''
    for arg in args:
        for char in arg:
            if char.lower() not in acceptables:
                return False
    return True

# 
def printer(*args):
    '''
        Takes arguments like that in print and returns string like print() function
    '''
    returner=''
    for posa, arg in enumerate(args):
        if type(arg) in (list, tuple):
            for posi, item in enumerate(arg):
                returner+=(", " if posi!=0 else "\n\t")+item+("\n" if posi==len(arg)-1 else "")
        else:
            returner+=(" " if not returner[-1:]=="\n" and posa!=0 else "")+arg
    return returner

def return_rooms():
    pass


if __name__ == '__main__':
    print(availableRooms())