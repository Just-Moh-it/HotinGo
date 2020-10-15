import tkinter as tk
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

def checkUser(username, password):
    cursor.execute("Select count(username) from login where username='%s' and password='%s';" %(username, password))
    return cursor.fetchone()[0]>=1


cursor.execute("select * from login;")
print(cursor.fetchall())


# ==============Tkinter================

# Tkinter functions------------
def login(username, password):
    if checkUser(username, password):
        print("Logged in successfully")
        root.destroy()
    else:
        label_invalid.widget.pack()
        # label_invalid.widget.pack_forget()



# Window definition------------

win=tk.Tk()
win.geometry("400x170+500+300")

# Login Frame
frame_login=tk.Frame(win)
frame_login.place(x=40, y=40)

# Username tb
tk.Label(frame_login, text="Username").grid(row=0, column=0)

username=tk.StringVar()
username_tb=tk.Entry(frame_login, textvariable=username)
username_tb.grid(row=0, column=1)

# Password tb
tk.Label(frame_login, text="Password").grid(row=1, column=0)

password=tk.StringVar()
password_tb= tk.Entry(frame_login, textvariable=password, show="•")
password_tb.grid(row=1, column=1)

# Login Button
login_button=tk.Button(frame_login, text="Login", height=2, width=8, onclick=login)
login_button.grid(row=2, column=1, pady=10)

win.mainloop()