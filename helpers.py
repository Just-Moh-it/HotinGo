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
    cmd=None
    a=cursor.fetchone()[0]>=1
    return a 



def updatePassword(username, sec_ans, sec_que, password):
    cmd=f"update login set password='{password}' where username='{username}' and sec_ans='{sec_ans}' and sec_que='{sec_que}' limit 1;"
    cursor.execute(cmd)
    cmd=f"select count(username) from login where username='{username}' and password='{password}' and sec_ans='{sec_ans}' and sec_que='{sec_que}';"
    cursor.execute(cmd)
    return cursor.fetchone()[0]>=1

def updateUsername(oldusername, password, newusername):
    cmd=f"update login set username='{newusername}' where username='{oldusername}' and password='{password}' limit 1;"
    cursor.execute(cmd);
    cmd=f"select count(username) from login where username='{newusername}' and password='{password}''"
    cursor.execute(cmd)
    return cursor.fetchone()[0]>=1

def availableRooms(status='v'):
    # Returns number of rooms either booked or unbooked
    # Status can be 'b' for booked or 'v' for vacant ot total by default for total rooms
    if status.casefold()=='b':
        cursor.execute("select count(room_id) from rooms where currently_booked='1';")
    elif status.casefold()=='t':
        cursor.execute("select count(room_id) from rooms")
    else:
        cursor.execute("select count(room_id) from rooms where currently_booked='0';")
    return cursor.fetchone()[0]

def totalamount(roomno):
    cmd = "select datediff(check_in , check_out) * rooms.price from reservations, rooms where reservations.room_id = rooms.room_id and rooms.room_no = roomno;"
    cursor.execute(cmd)
    return str(cursor.fetchone()[0])

def addguest(name,address,city,email_id,phone,Dlicense):
    cmd = f'insert into guests(name,address,email_id,city,phone,Driving_License) values({name},{address},{email_id},{city},{phone},{Dlicense});'
    cursor.execute(cmd)
    

def find_g_id(name):
    cmd = f"select g_id from guests where name = {name}"
    cursor.execute(cmd)
    return cursor.fetchone()[0]

def checkin(g_id):
    cmd = f"select * from reservations where g_id = {g_id}"
    cursor.execute(cmd)
    return cursor.fetchall()


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