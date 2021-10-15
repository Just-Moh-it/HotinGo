import mysql.connector
import os
import matplotlib.pyplot as pt
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

cursor=connection.cursor(buffered=True)

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

# def reserve(r_id,g_id,meal,room_id,r_type):
#     cmd1 = f"insert into reservations values('{r_id}','{g_id}',curdate(),Null,Null,'{meal}','{room_id}','{r_type}')"
#     cmd2 = f"update rooms set currently_booked = 1 where room_id = '{room_id}'"
#     cursor.execute(cmd2)
#     cursor.execute(cmd1)
#     return cursor.fetchall()

def checkout(id):
    cmd = f'update reservations set check_out=current_timestamp where id={id} limit 1;'
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return True

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

def get_details(r_id):
        cmd = f"select room_no,room_type,price from rooms where id = {r_id};"
        cursor.execute(cmd)
        print(cursor.fetchall())


# Get all guests
def get_guests():
    cmd = "select id, name, address, email_id, phone, city, created_at from guests;"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return cursor.fetchall()

# Add a guest
def add_guest(name,address,email_id,phone):
    cmd = f"insert into guests(name,address,email_id,phone) values('{name}','{address}','{email_id}',{phone});"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return True

# add a room
def add_room(room_no,price,room_type):
    cmd = f"insert into rooms(room_no,price,room_type) values('{room_no}',{price},'{room_type}');"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return True

# Get All rooms
def get_rooms():
    cmd = "select id, room_no, room_type, price, created_at from rooms;"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return cursor.fetchall()

# Get all reservations
def get_reservations():
    cmd = "select id, g_id, r_id, check_in, check_out, meal from reservations;"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return cursor.fetchall()

# Add a reservation
def add_reservation(g_id,meal,r_id,check_in='now'):
    cmd = f"insert into reservations(g_id,check_in,r_id, meal) values('{g_id}',{f'{chr(39) + check_in + chr(39)}' if check_in != 'now' else 'current_timestamp'},'{meal}','{r_id}');"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return True

# Get all room count
def get_total_rooms():
    cmd = "select count(room_no) from rooms;"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return cursor.fetchone()[0]

# Check if a room is vacant
def vacant():
   cmd = f"select count(ros.id) from reservations rs, rooms ros where rs.r_id = ros.id and rs.check_out is Null;"
   cursor.execute(cmd)
   return cursor.fetchone()[0]

def booked():
    return (get_total_rooms() - vacant())

def bookings():
    cmd = f"select count(rs.id) from reservations rs , rooms ros where rs.r_id = ros.id and ros.room_type = 'D'"
    cursor.execute(cmd)
    deluxe  = cursor.fetchone()[0]
    cmd1 = f"select count(rs.id) from reservations rs , rooms ros where rs.r_id = ros.id and ros.room_type = 'N'"
    cursor.execute(cmd1)
    Normal  = cursor.fetchone()[0]
    return [deluxe,Normal]


# Get total money earned till date
def get_total_money_earned():
    cmd = "select sum(price) from reservations as rs, rooms as rm where rs.r_id = rm.id;"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    return cursor.fetchone()[0]

# Get total hotel value
def get_total_hotel_value():
    cmd = "select sum(price) from rooms;"
    cursor.execute(cmd)
    if cursor.rowcount==0:
        return False
    value =  cursor.fetchone()[0]
    if value >= 1000:
        return str(value/1000)+'k'
    elif value >= 1000000:
        return str(value/1000000)+'m'


def delete_reservation(id):
    cmd = f"delete from reservations where id='{id}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True

def delete_room(id):
    cmd = f"delete from rooms where id='{id}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True

def delete_guest(id):
    cmd = f"delete from guests where id='{id}';"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True

def update_rooms(room_no,room_type,price):
    cmd = f"update rooms set room_type = '{room_type}',price= {price}  where room_no = {room_no};"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
            return False
    return True

def update_guests(name,address,id,phone):
    print(name,address,id)
    cmd = f"update guests set address = {address},phone = {phone} , name = {name} where id = {id};"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
            return False
    return True

def update_reservations(g_id,check_in,room_id,reservation_date,check_out,meal,type,id):
    cmd = f"update reservations set check_in = '{check_in}',check_out = '{check_out}',g_id = {g_id}, \
        r_date = '{reservation_date}',meal = {meal},r_type='{type}', r_id = {room_id} where id= {id};"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
            return False
    return True

def meals():
    cmd = f"select sum(meal) from reservations;"
    cursor.execute(cmd)
    meals =  cursor.fetchone()[0]
    if meals < 1000:
        return meals
    elif meals >= 1000:
        return str(meals/1000)+'k'
    elif meals >= 1000000:
        return str(meals/1000000)+'m'

def rooms_chart():
    pt.pie([vacant(),booked()],[.1,.1],startangle=-30,colors=('#6495ED','#8A8A8A'))
    pt.show()

def bookings_chart():
    pt.pie(bookings,[.1,.1],startangle=-30,colors=('#6495ED','#8A8A8A'))
    pt.show()
