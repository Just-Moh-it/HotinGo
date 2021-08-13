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
    cmd = f"Select count(username) from login where username='{username}' and BINARY password='{password}'"
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

# def availableRooms(status='v'):
#     # Returns number of rooms either booked or unbooked
#     # Status can be 'b' for booked or 'v' for vacant ot total by default for total rooms
#     if status.casefold()=='b':
#         cursor.execute("select count(id) from rooms where currently_booked='1';")
#     elif status.casefold()=='t':
#         cursor.execute("select count(id) from rooms")
#     else:
#         cursor.execute("select count(id) from rooms where currently_booked='0';")
#     return cursor.fetchone()[0]

def totalamount(room_no):
    cmd = f"select datediff(check_out , check_in) * rooms.price from reservations, rooms where reservations.room_id = rooms.room_id and rooms.room_id = '{room_no}';"
    cursor.execute(cmd)
    return str(cursor.fetchone()[0])


def find_g_id(name):
    cmd = f"select g_id from guests where name = '{name}'"
    cursor.execute(cmd)
    out =  cursor.fetchone()[0]
    return out

def checkin(g_id):
    cmd = f"select * from reservations where g_id = '{g_id}';"
    cursor.execute(cmd)
    reservation =  cursor.fetchall()
    if reservation != []:
        subcmd = f"update reservations set check_in = curdate() where g_id = '{g_id}' "
        cursor.execute(subcmd)
        return 'successful'
    else:
        return 'No reservations for the given Guest'

def reserve(r_id,g_id,meal,room_id,r_type):
    cmd1 = f"insert into reservations values('{r_id}','{g_id}',curdate(),Null,Null,'{meal}','{room_id}','{r_type}')"
    cmd2 = f"update rooms set currently_booked = 1 where room_id = '{room_id}'"
    cursor.execute(cmd2)
    cursor.execute(cmd1)
    return cursor.fetchall()

def checkout(roomno):
    cmd1 = f"update reservations set check_out = curdate() where room_id = '{roomno}' "
    cmd2 = f"update rooms set currently_booked = 0 where room_id = '{roomno}' "
    cursor.execute(cmd1)
    cursor.execute(cmd2)
    return totalamount(roomno)

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


# Get all guests
def get_guests():
    cmd = "select id, name, address, email_id, phone, city, created_at from guests;"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return cursor.fetchall()

# Add a guest
def add_guest(name,address,city,email_id,phone):
    cmd = f"insert into guests(name,address,email_id,city,phone) values('{name}','{address}','{email_id}','{city}',{phone});"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return True

# add a room
def add_room(room_no,price,room_type):
    cmd = f"insert into rooms(room_no,price,type) values('{room_no}',{price},'{room_type}');"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return True

# Get All rooms
def get_rooms():
    cmd = "select id, room_no, price, type, created_at from rooms;"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return cursor.fetchall()

# Get all reservations
def get_reservations():
    cmd = "select id, g_id, check_in, check_out, meal, r_id, created_at from reservations;"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return cursor.fetchall()

# Add a reservation
def add_reservation(g_id,check_in,meal,r_id):
    cmd = f"insert into reservations(g_id,check_in,meal,r_id) values('{g_id}','{check_in}','{meal}','{r_id}');"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return True
