import tkinter as tk
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
    cursor.execute("Select count(username) from login where username='%s' and password='%s';" %(username, password))
    return cursor.fetchone()[0]>=1


# ==============Tkinter================

# Tkinter functions------------
def login():
    if checkUser(username.get(), password.get()):
        print("Logged in successfully")
        win.destroy()
    else:
        messagebox.showerror(title="Invalid Credentials", message="The username and password don't match")


# Window definition-------------

win=tk.Tk()
win.title("Login-Hotel Management System")
win.geometry("290x150")
win.resizable(0,0)


# Login Frame
frame_login=tk.Frame(win)
frame_login.place(x=40, y=40)

# Username tb
tk.Label(frame_login, text="Username ").grid(row=0, column=0)

username=tk.StringVar()
username_tb=tk.Entry(frame_login, textvariable=username)
username_tb.grid(row=0, column=1)

# Password tb
tk.Label(frame_login, text="Password ").grid(row=1, column=0)

password=tk.StringVar()
password_tb= tk.Entry(frame_login, textvariable=password, show="•")
password_tb.grid(row=1, column=1)

# Invalid Label
invalid_message=tk.StringVar()
invalid_label=tk.Label(frame_login, textvariable=invalid_message)

# Login Button
login_button=tk.Button(frame_login, text="Login", height=1, width=8, command=login)
login_button.grid(row=2, column= 1, pady=10)

win.mainloop()

