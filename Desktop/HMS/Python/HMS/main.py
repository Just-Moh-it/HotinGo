from tkinter import messagebox
import tkinter as tk
import tkinter.font as font
from sqlconnect import *

# ==============Tkinter================

# Tkinter functions------------

secques=["Where were you born?", 
    "What was the first movie you watched at the cinemas?",
    "What was your first pet's name?",
    "What is your favourite dish?",
    "What brand was your first car of?"]

''' ------------------Window generators---------------------'''
def loginWindow():
    # Login check function
    def login_func():
        if checkUser(username.get(), password.get()):            
            messagebox.showinfo(title="Successfull", message="Login Successfull")
            login.destroy()
            
        else:
            messagebox.showerror(title="Invalid Credentials", message="The username and paswword don't match")
    
    # Signup Button Function
    def signup_btn():
        login.destroy()
        signUpWindow()

    # ----------------Window------------------
    login=tk.Tk()
    login.title("Login-Hotel Management System")
    login.geometry("400x180+560+300")
    login.resizable(0,0)


    # Login Frame
    frame_login=tk.Frame(login)
    frame_login.place(x=40, y=40)

    # Heading

    heading=tk.Label(frame_login, text="Login").grid(row=0, column=1)
    heading['font']=header_font
    heading.grid(row=0, column=1)

    # Username tb
    tk.Label(frame_login, text="Username").grid(row=1, column=0)

    username=tk.StringVar(login)
    username_tb=tk.Entry(frame_login, textvariable=username)
    username_tb.grid(row=1, column=1,columnspan=2)


    # Password tb
    tk.Label(frame_login, text="Password").grid(row=2, column=0)

    password=tk.StringVar(login)
    password_tb= tk.Entry(frame_login, textvariable=password, show="•")
    password_tb.grid(row=2, column=1,columnspan=2)


    # Login Button
    login_button=tk.Button(frame_login, text="Login", height=2, width=8, command=login_func)
    login_button.grid(row=3, column=1,pady=10)

    # SignUp button
    signup_button=tk.Button(frame_login, text="SignUp", height=2, width=8, command=signup_btn)
    signup_button.grid(row=3, column=2,pady=10)

def signUpWindow():

    # -------------Constructor-----------------
    signup=tk.Tk()
    signup.geometry("400x400+500+200")
    signup.resizable(0,0)

    # --------------Tkinter layout--------------

    # Main Frame
    frame_signup=tk.Frame(signup)
    frame_signup.place(padx=20, pady=50, ipadx=40, ipadyy=40)
    
    # Header
    header=tk.Label(frame_signup, text="Sign Up").grid(row=0, column=1)
    header['font']=header_font
    header.grid(row=0, column=1)

    # Name
    tk.Label(frame_signup, text="Full Name").grid(row=1, column=0)

    nname=tk.StringVar(signUpWindow)
    nname_tb=tk.Entry(frame_signup, textvariable=nname)
    nname_tb.grid(row=1, column=1)

# Globally accessed variables across main.py

# header_font=font.Font(weight="bold", family="Arial", size=18)
header_font = font.Font(size=30)

root= tk.Tk()
root.withdraw()
loginWindow()
root.mainloop()

