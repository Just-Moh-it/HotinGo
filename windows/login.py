from tkinter import messagebox
import tkinter as tk
from config import fonts
from controller import *
from .main_panels.main_window import MainWindow
from .forgot_password import *

def loginWindow():
    ''' Login Window Tkinter '''

    global user
    # Login check function
    def loginFunc():
        global user
        if '"' in username.get() or '"' in password.get() or "'" in username.get() or "'" in password.get():
            reset()
            messagebox.showerror("Invalid", "Username or password can not contain \" or \' ")
            return
        if checkUser(username.get().lower(), password.get()):
            login.destroy()
            user=username.get().lower()
            MainWindow()
        else:
            messagebox.showerror(title="Invalid Credentials", message="The username and password don't match")
            reset(password)


    # Forgot Password Button
    def forgotPwd():
        login.destroy()
        forgotPwdWindow()

    # Clears all StringVars
    def reset(*args):
        if args==():
            username.set(""); password.set("") # Clears all inputs
        for arg in args:
            arg.set("")


    # ----------------Window------------------
    login=tk.Tk()
    login.title("Login-Hotel Management System")
    login.geometry("370x180+535+310")
    login.resizable(0,0)
    login['background']='white'

    # Login Frame
    frame_login=tk.Frame(login, background='white')
    frame_login.place(x=20, y=10)

    # Heading
    tk.Label(frame_login, text="Login", font=fonts.get('h1')).grid(row=0, column=0, columnspan=2, padx=(60,0), pady=(0,10))

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
    tk.Button(frame_login, text="Login", height=2, width=9, command=loginFunc).grid(row=3, column=0, columnspan=2, pady=10, padx=(0,150))

    # Forgot Password Button
    tk.Button(frame_login, text="Reset Pwd", height=2, width=9, command=forgotPwd).grid(row=3, column=0, columnspan=2, pady=10, padx=(150, 0))

    # Or label
    tk.Label(frame_login, text='or').grid(row=3, column=0, columnspan=2, pady=10, padx=(110,0))
