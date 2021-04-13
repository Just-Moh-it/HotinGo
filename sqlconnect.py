import mysql.connector

# ===================SQL Connectivity=================

# SQL Connection
try: 
    connection=mysql.connector.connect(host="remotemysql.com", 
                                user="vBSRv3edd7", 
                                password="WybOhrwfxF", 
                                database = "vBSRv3edd7", 
                                port="3306", autocommit=True)
except mysql.connector.errors.ProgrammingError:
    print("!!!! Database Authentication Failed, update credentails in sqlconnect.py\n     or see references/db.txt for pass")
    quit()

"""connection=mysql.connector.connect(user="root", 
                            password="mohit123", 
                            database = "hms", 
                            autocommit=True)"""

cursor=connection.cursor()

# SQL functions

def checkUser(username, password=None):
    cmd="Select count(username) from login where username='"+username.lower()+(("' and BINARY password='"+password) if password is not None else "")+"';"
    cursor.execute(cmd)
    cmd=None
    a=cursor.fetchone()[0]>=1
    return a 

def addUser(username, password, sec_que, sec_ans):
    cmd=f"Insert into login (username, password, sec_que, sec_ans) values ('{username}', '{password}', '{sec_que}', '{sec_ans}');"
    cursor.execute(cmd)
    cmd=f"select count(username) from login where username='{username}' and password='{password}' and sec_que='{sec_que}' and sec_ans='{sec_ans}'"
    cursor.execute(cmd)
    cmd=None
    return cursor.fetchone()[0]>=1

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

def totalMoney():
    # sum of all bookings 
    # to be done by @anirudh agarwal cursor.execute("select from reservations, rooms where reservations.room_id=rooms.room_id")
    return str(cursor.fetchone()[0])

def totalValue():
    cursor.execute("select sum(price) from rooms")
    return str(cursor.fetchone()[0])
