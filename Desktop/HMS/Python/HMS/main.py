from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
import tkinter.font as font
from sqlconnect import *

#============Python Functions==========

# If the characters in StringVars passed as arguments are in acceptables return True, else returns False
def acceptable(*args, acceptables=(*[chr(i) for i in range(97,123)], "_",*[str(i) for i in range(10)], ".")):
    for arg in args:
        for char in arg:
            if char.lower() not in acceptables:
                return False
    return True

# Takes arguments like that in print and returns string like print() function
def printer(*args):
    returner=''
    for posa, arg in enumerate(args):
        if type(arg) in (list, tuple):
            for posi, item in enumerate(arg):
                returner+=(", " if posi!=0 else "\n\t")+item+("\n" if posi==len(arg)-1 else "")
        else:
            returner+=(" " if not returner[-1:]=="\n" and posa!=0 else "")+arg
    return returner



# ==============Tkinter================

# Tkinter functions------------

''' ------------------Window generators---------------------'''
def loginWindow():
    # Login check function
    def loginFunc():
        if checkUser(username.get().lower(), password.get()):            
            messagebox.showinfo(title="Successfull", message="Login Successfull")
            login.destroy()
            
        else:
            messagebox.showerror(title="Invalid Credentials", message="The username and paswword don't match")
            reset(password)
    
    # Signup Button Function
    def signupBtn():
        login.destroy()
        signUpWindow()

    # Clears all StringVars
    def reset(*args):
        if args==():
            username.set(""); password.set("") # Clears all inputs
        for arg in args:
            arg.set("")


    # ----------------Window------------------
    login=tk.Tk()
    login.title("Login-Hotel Management System")
    login.geometry("370x200+560+300")
    login.resizable(0,0)


    # Login Frame
    frame_login=tk.Frame(login)
    frame_login.place(x=40, y=20)

    # Heading
    header_font=font.Font(login, size=28)
    header=tk.Label(frame_login, text="Login")
    header['font']=header_font
    header.grid(row=0, column=0, columnspan=2, padx=(60,0))

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
    login_button=tk.Button(frame_login, text="Login", height=2, width=8, command=loginFunc)
    login_button.grid(row=3, column=0, columnspan=2, pady=10, padx=(0, 25))

    # Or label
    tk.Label(frame_login, text='or').grid(row=3, column=0, columnspan=2, pady=10, padx=(75,0))

    # SignUp button
    signup_button=tk.Button(frame_login, text="SignUp", height=2, width=8, command=signupBtn)
    signup_button.grid(row=3, column=0, columnspan=2, pady=10, padx=(175,0))

def signUpWindow():
    header_font=font.Font(size=30)
    # -------------Constructor-----------------
    signup=tk.Tk()
    signup.title("Sign Up-Hotel Management System")
    signup.geometry("535x260+450+290")
    signup.resizable(0,0)
    signup.grid_propagate(False) # Won't work without this

    # --------------Tkinter Functions-----------
    
    # Login Button Function
    def loginBtn():
        signup.destroy()
        loginWindow()

    # Sign Up Button Function
    def signupFunc():
        if (not acceptable(username.get())) or (username.get()+' ').isspace():
            messagebox.showerror("Invalid-HMS", printer("Please enter a valid 'Username'. Valid usernames must only contain :", acceptables))
            username_tb.focus(); return
        elif len(password.get())<8 or password.get().isspace():
            messagebox.showerror("Invalid-HMS", printer("Please enter a valid 'Password'. Passwords must", ['• Contain 8 characters or more', "\n\t• Not be empty"]))
            print(username.get(), username.get().isspace())
            username_tb.focus(); return
        elif not name.get().lower().replace(" ", "").isalnum() or name.get().isspace():
            messagebox.showerror("Invalid-HMS", "Please enter a valid 'Full Name'")
            reset(name); return
        elif not sec_ans.get().lower().replace(" ", "").isalnum() or (sec_ans.get() in ("'", ";")) or sec_ans.get().isspace():
            messagebox.showerror("Invalid-HMS", "Please enter a valid 'Answer to security question'")
            reset(sec_ans); return
        
        # Check if updated
        if checkUser(username.get()):
            messagebox.showinfo("User Exists-HMS", "Username has been taken. Please try a different username.")
            username_tb.select_range(0,tk.END)
            return
        if addUser(name.get(), username.get().lower(), password.get(), sec_que.get(), sec_ans.get()):
            is_sucess=messagebox.askquestion("Sign Up successful-HMS", "Sign Up successful.\nProceed to login?", icon='info')
            if is_sucess=='yes': loginBtn()
            reset()
        else:
            messagebox.showerror("Sign Up Failed-HMS", "Signup failed because of an error")
    
    # Clears all StringVars
    def reset(*args):
        if args==():
            name.set(""); username.set(""); password.set(""); sec_ans.set("") # Clears all inputs
        for arg in args:
            arg.set("")

    # --------------Tkinter layout--------------

    # Main Frame
    frame_signup=tk.Frame(signup)
    frame_signup.place(x=17, y=10)
    frame_signup.columnconfigure(0, weight=6)
    frame_signup.columnconfigure(1, weight=25)

    
    # Heading
    header_font=font.Font(frame_signup, size=28)
    header=tk.Label(frame_signup, text="Sign Up")
    header['font']=header_font
    header.grid(row=0, column=0, columnspan=3, pady=(0,10))

    # Username tb
    tk.Label(frame_signup, text="Username").grid(row=1, column=0)

    username=tk.StringVar(signup)
    username_tb=tk.Entry(frame_signup, textvariable=username, width=40)
    username_tb.grid(row=1, column=1)

    # Password tb
    tk.Label(frame_signup, text="Password").grid(row=2, column=0)

    password=tk.StringVar(signup)
    password_tb= tk.Entry(frame_signup, textvariable=password, show="•", width=40)
    password_tb.grid(row=2, column=1)
    
    # Full Name tb
    tk.Label(frame_signup, text="Full Name").grid(row=3, column=0)

    name=tk.StringVar(signup)
    name_tb=tk.Entry(frame_signup, textvariable=name, width=40)
    name_tb.grid(row=3, column=1)

    # Security Questions cb
    tk.Label(frame_signup, text="Security Question").grid(row=4, column=0)

    sec_que=tk.StringVar(signup)
    sec_que.set(sec_ques[0])
    sec_que_cb=tk.OptionMenu(frame_signup, sec_que, *sec_ques)
    sec_que_cb['width']=38
    sec_que_cb.grid(row=4, column=1)

    # Security Answer tb
    tk.Label(frame_signup, text="Answer").grid(row=5, column=0)

    sec_ans=tk.StringVar(signup)
    sec_ans_tb= tk.Entry(frame_signup, textvariable=sec_ans, width=40)
    sec_ans_tb.grid(row=5, column=1)

    # SignUp button
    signup_button=tk.Button(frame_signup, text="SignUp", height=2, width=8, command=signupFunc)
    signup_button.grid(row=6, column=0, columnspan=3, pady=10, padx=(0,140))

    # Login Button
    login_button=tk.Button(frame_signup, text="Login", height=2, width=8, command=loginBtn)
    login_button.grid(row=6, column=0, columnspan=3, pady=10, padx=(30,0))
    
    # Reset Button
    reset_button=tk.Button(frame_signup, text="Reset", height=2, width=8, command=lambda : reset())
    reset_button.grid(row=6, column=0, columnspan=3, pady=10, padx=(200,0))

def mainWindow():
    

# Globally accessed variables across main.py
sec_ques=("What was the first movie you watched at the cinemas?",
    "Where were you born?",
    "What was your first pet's name?",
    "What is your favourite dish?",
    "What brand was your first car of?",
    "what is your favourite movie?",
    "What is your favourite colour")

acceptables=(*[chr(i) for i in range(97,123)], "_",*[str(i) for i in range(10)], ".")

# Main window constructor
root = tk.Tk()
root.withdraw()
signUpWindow()
root.mainloop()