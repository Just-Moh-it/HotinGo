from tkinter import messagebox
import tkinter as tk
import tkinter.font as font
from models import *
from sqlconnect import *


# ==============Tkinter================

# Tkinter functions------------

''' ------------------Window generators---------------------'''
def loginWindow():


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
            mainWindow()
        else:
            messagebox.showerror(title="Invalid Credentials", message="The username and password don't match")
            reset(password)
    
    # Signup Button Function
    def signupBtn():
        login.destroy()
        signUpWindow()

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

    h1_font=font.Font(login, size=20, family='arial', weight='bold')

    # Login Frame
    frame_login=tk.Frame(login, background='white')
    frame_login.place(x=20, y=10)

    # Heading
    tk.Label(frame_login, text="Login", font=h1_font).grid(row=0, column=0, columnspan=2, padx=(60,0), pady=(0,10))

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
    tk.Button(frame_login, text="Login", height=2, width=9, command=loginFunc).grid(row=3, column=0, columnspan=2, pady=10, padx=(0,180))

    # Forgot Password Button
    tk.Button(frame_login, text="Forgot Pwd?", height=2, width=9, command=forgotPwd).grid(row=3, column=0, columnspan=2, pady=10)
 
    # Or label
    tk.Label(frame_login, text='or').grid(row=3, column=0, columnspan=2, pady=10, padx=(110,0))

    # SignUp button
    tk.Button(frame_login, text="SignUp ☞", height=2, width=9, command=signupBtn).grid(row=3, column=0, columnspan=2, pady=10, padx=(210,0))


def signUpWindow():
    h1_font=font.Font(size=20, weight='bold', family='arial')
    # -------------Constructor-----------------
    signup=tk.Tk()
    signup.title("Sign Up-Hotel Management System")
    signup.geometry("535x230+450+290")
    signup.resizable(0,0)
    signup['background']='white'
    signup.grid_propagate(False) # Won't work without this

    # --------------Tkinter Functions-----------
    
    # Login Button Function
    def loginBtn():
        signup.destroy()
        loginWindow()

    # Sign Up Button Function
    def signupFunc():
        if (not acceptable(username.get())) or (username.get()+' ').isspace() or len(username.get()) not in range(3,15):
            messagebox.showerror("Invalid-HMS", printer("Please enter a valid 'Username'. Valid usernames\n•Should be between 3 and 15 characters long.\n•Must only contain :", acceptables))
            username_tb.focus(); return
        if len(password.get()) not in range(8, 30) or password.get().isspace():
            messagebox.showerror("Invalid-HMS", printer("Please enter a valid 'Password'. Passwords must", ['• Contain 8 to 30 characters', "\n\t• Not be empty"]))
            password_tb.focus(); return
        if sec_ans.get().isspace() or len(sec_ans.get()) not in range(0,30):
            messagebox.showerror("Invalid-HMS", "Please enter a valid 'Answer to security question'. Must contain less than 30 characters.")
            reset(sec_ans); return
        
        # Check if updated
        if checkUser(username.get()):
            messagebox.showinfo("User Exists-HMS", "Username has been taken. Please try a different username.")
            username_tb.select_range(0,tk.END)
            return
        if addUser(username.get().lower(), password.get(), sec_que.get(), sec_ans.get()):
            is_sucess=messagebox.askyesno("Sign Up successful-HMS", "Sign Up successful.\nProceed to login?", icon='info')
            if is_sucess==True: loginBtn()
            reset()
        else:
            messagebox.showerror("Sign Up Failed-HMS", "Signup failed because of an error")
    
    # Clears all StringVars
    def reset(*args):
        if args==():
            username.set(""); password.set(""); sec_ans.set("") # Clears all inputs
        for arg in args:
            arg.set("")

    # --------------Tkinter layout--------------

    # Main Frame
    frame_signup=tk.Frame(signup, background='white')
    frame_signup.place(x=17, y=10)
    frame_signup.columnconfigure(0, weight=6)
    frame_signup.columnconfigure(1, weight=25)

    
    # Heading
    h1_font=font.Font(frame_signup, size=20, weight='bold', family='arial')
    header=tk.Label(frame_signup, text="Sign Up")
    header['font']=h1_font
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

    # Security Questions cb
    tk.Label(frame_signup, text="Security Question").grid(row=3, column=0)

    sec_que=tk.StringVar(signup)
    sec_que.set(sec_ques[0])
    sec_que_cb=tk.OptionMenu(frame_signup, sec_que, *sec_ques)
    sec_que_cb['width']=38
    sec_que_cb.grid(row=3, column=1)

    # Security Answer tb
    tk.Label(frame_signup, text="Answer").grid(row=4, column=0)

    sec_ans=tk.StringVar(signup)
    sec_ans_tb= tk.Entry(frame_signup, textvariable=sec_ans, width=40)
    sec_ans_tb.grid(row=4, column=1)

    # SignUp button
    signup_button=tk.Button(frame_signup, text="SignUp", height=2, width=8, command=signupFunc)
    signup_button.grid(row=5, column=0, columnspan=3, pady=10, padx=(0,140))

    # Login Button
    login_button=tk.Button(frame_signup, text="Login", height=2, width=8, command=loginBtn)
    login_button.grid(row=5, column=0, columnspan=3, pady=10, padx=(30,0))
    
    # Reset Button
    reset_button=tk.Button(frame_signup, text="Reset", height=2, width=8, command=lambda : reset())
    reset_button.grid(row=5, column=0, columnspan=3, pady=10, padx=(200,0))

def forgotPwdWindow():

    def loginBtn():
        forgot_pwd.destroy()
        loginWindow()
    
    def changePwd():
        if not checkUser(username.get()):
            messagebox.showerror("Invalid username", "Please enter a valid username"); return
        elif 30<len(password.get())<8 or password.get().isspace():
            messagebox.showerror("Invalid-HMS", printer("Please enter a valid 'Password'. Passwords must", ['• Contain 8 characters or more', "\n\t• Not be empty"]))
            username_tb.focus(); return

        if updatePassword(username.get().lower(), sec_ans.get(), sec_que.get(), password.get()):
            login=messagebox.askyesno("Successful", "Password Changed successfully. Proceed to login?")
            if login==True:
                loginBtn(); return
        else:
            messagebox.showerror("Error", "Record with the following details not found."); return


    # ------------Constructor--------------
    forgot_pwd=tk.Tk()
    forgot_pwd.title("Reset Password-Hotel Management System")
    forgot_pwd.geometry("535x240+450+285")
    forgot_pwd.resizable(0,0)
    forgot_pwd['background']='white'

    h1_font=font.Font(forgot_pwd, size=20, family='arial', weight='bold')

    # Main Frame
    frame_forgot_pwd=tk.Frame(forgot_pwd, background='white')
    frame_forgot_pwd.place(x=20, y=25)

    # Heading
    tk.Label(frame_forgot_pwd, text="Reset Password", font=h1_font).grid(row=0, column=0, columnspan=2, padx=(60,0))

    # Username tb
    tk.Label(frame_forgot_pwd, text="Username").grid(row=1, column=0)

    username=tk.StringVar(forgot_pwd)
    username_tb=tk.Entry(frame_forgot_pwd, textvariable=username, width=40)
    username_tb.grid(row=1, column=1)
    
    # Security Questions cb
    tk.Label(frame_forgot_pwd, text="Security Question").grid(row=2, column=0)

    sec_que=tk.StringVar(forgot_pwd)
    sec_que.set(sec_ques[0])
    sec_que_cb=tk.OptionMenu(frame_forgot_pwd, sec_que, *sec_ques)
    sec_que_cb['width']=38
    sec_que_cb.grid(row=2, column=1)

    # Password tb
    tk.Label(frame_forgot_pwd, text="Security Answer").grid(row=3, column=0)

    sec_ans=tk.StringVar(forgot_pwd)
    sec_ans_tb= tk.Entry(frame_forgot_pwd, textvariable=sec_ans, width=40)
    sec_ans_tb.grid(row=3, column=1)

    # Password tb
    tk.Label(frame_forgot_pwd, text="Set New Pasword").grid(row=4, column=0)

    password=tk.StringVar(forgot_pwd)
    password_tb=tk.Entry(frame_forgot_pwd, textvariable=password, width=40)
    password_tb.grid(row=4, column=1)

    offset=60

    # Change Password Button
    change_pwd_button=tk.Button(frame_forgot_pwd, text="Change\nPassword", height=2, width=12, command=lambda : changePwd())
    change_pwd_button.grid(row=5, column=0, columnspan=2, pady=10, padx=(0,120-offset))

    # Login Button
    login_button=tk.Button(frame_forgot_pwd, text="Login", height=2, width=12, command=loginBtn)
    login_button.grid(row=5, column=0, columnspan=2, pady=10, padx=(120+offset,0))


def mainWindow():
    # -----------functions-------------------

    # -----------Constructor------------------
    main=tk.Tk()
    main.title("Main-Hotel Management System")
    main.geometry("840x400+300+200")
    main.grid_propagate(False)
    main.resizable(0,0)
    main.iconbitmap("icon.ico")
    
    # For testing purposes only. Remove in final build to reduce unauthorized access
    """ try: user
    except NameError: user='admin' """

    # ----------Variables--------------------
    h1_font=font.Font(main, size=20, weight='bold', family='Arial')
    h2_font=font.Font(main, size=15, weight='bold', family='Arial')


    # --------------Tkinter Function--------------
    def home():
        panel_side.place(y=button_dashboard.winfo_y()+2)
        info_header.configure(text='Dashboard')
    def reserve():
        panel_side.place(y=button_reserve.winfo_y()+2)
        info_header.configure(text='Reserve')
    def rooms():
        panel_side.place(y=button_rooms.winfo_y()+2)
        info_header.configure(text='Rooms')
    def payment():
        panel_side.place(y=button_payment.winfo_y()+2)
        info_header.configure(text='Payement')
    def account():
        panel_side.place(y=button_account.winfo_y()+2)
        info_header.configure(text='Account')
    def logout():
        confirm=messagebox.askyesno('Confirm log-out', "Do you really want to log out?")
        if confirm==True:
            user=None
            loginWindow()
            main.destroy()

    # ---Navigation Frame---
    frame_navigation=tk.Frame(main, background='white')
    frame_navigation.place(x=0, y=0, width=170, height=400)

    #---Main Frame---
    frame_main=tk.Frame(main, background='white')
    frame_main.place(x=170, y=0, width=670, height=400)

    # Header
    header_main=tk.Label(frame_navigation, text="Hotel\nManagement\nSystem", background='white')
    header_main.pack(fill=tk.X, pady=(30,0))
    header_main['font']=h1_font

    # Side Panel
    panel_side=tk.Frame(frame_navigation, background='#c32148', height=32, width=5)
    panel_side.place(x=0,y=0)

    # ---Navigation Buttons and Title---

    # Buttons
    button_dashboard=tk.Button(frame_navigation, text="Dashboard", command=home, height=2, relief=tk.FLAT, background='white')
    button_dashboard.pack(fill=tk.X, pady=(25,0), padx=(4,0))

    button_reserve=tk.Button(frame_navigation, text="Reserve", command=reserve, height=2, relief=tk.FLAT, background='white')
    button_reserve.pack(fill=tk.X, padx=(4,0))

    button_rooms=tk.Button(frame_navigation, text="Rooms", command=rooms, height=2, relief=tk.FLAT, background='white')
    button_rooms.pack(fill=tk.X, padx=(4,0))

    button_payment=tk.Button(frame_navigation, text="Payment", command=payment, height=2, relief=tk.FLAT, background='white')
    button_payment.pack(fill=tk.X, padx=(4,0))

    button_account=tk.Button(frame_navigation, text="Account", command=account, height=2, relief=tk.FLAT, background='white')
    button_account.pack(fill=tk.X, padx=(4,0))

    button_logout=tk.Button(frame_navigation, text="Log out", command=logout, height=2, relief=tk.FLAT, background='white')
    button_logout.pack(fill=tk.X, padx=20, pady=(30,0))

    # Placing sidebar on dashboard
    panel_side.place(y=134)

    # --------------Work Frames and controls------------------
    # ---Top Frame---
    frame_header=tk.Frame(frame_main, width=630, height=40, pady=10)
    frame_header.place(x=0, y=0)

    # Frame_name Header
    info_header=tk.Label(frame_header, text="Dashboard")
    info_header['font']=h1_font
    info_header.place(x=2)

    # Logged in as label
    try: user
    except: user='admin'
    header_main=tk.Label(frame_header, text="Logged in as: " + user, background='white')
    header_main.place(x=465, y=5)
    header_main['font']=h2_font

    # ---Dashboard---
    frame_dashboard=tk.Frame(frame_main)
    frame_dashboard.place(x=0, y=40, width=630, height=400)

    backs=['#FF0013', '#FF9100', '#FFC200', '#00B950', '#0090F7', '#4842B8', '#AD00B1']

    tk.Label(frame_dashboard, font=h2_font, text='Statistics').grid(row=0, column=0, pady=3, sticky='w')

    frame_flow_right=tk.Frame(frame_dashboard)
    frame_flow_right.grid(row=1, column=0)

    widget_no=0 # For keeping track of no. of widgets made

    # Available rooms box
    parent_frame=tk.Frame(frame_flow_right, background=backs[widget_no], height=120, width=120)
    parent_frame.grid(row=0, column=widget_no, padx=5)

    label=tk.Label(parent_frame, text='Vacant\nRooms', background=backs[widget_no], foreground='white')
    label.pack(pady=(10,0), padx=12, fill=tk.BOTH)
    label['font']=h2_font

    label_av_rooms=tk.Label(parent_frame, text=availableRooms(), background=backs[widget_no], foreground='white')
    label_av_rooms.pack(fill=tk.BOTH)
    label_av_rooms['font']=h1_font

    widget_no+=1

    # Booked rooms box
    parent_frame=tk.Frame(frame_flow_right, background=backs[widget_no], height=120, width=120)
    parent_frame.grid(row=0, column=widget_no, padx=5)

    label=tk.Label(parent_frame, text='Booked\nRooms', background=backs[widget_no], foreground='white')
    label.pack(pady=(10,0), padx=12, fill=tk.BOTH)
    label['font']=h2_font

    label_av_rooms=tk.Label(parent_frame, text=availableRooms('b'), background=backs[widget_no], foreground='white')
    label_av_rooms.pack(fill=tk.BOTH)
    label_av_rooms['font']=h1_font

    widget_no+=1
    
    # Total rooms box
    parent_frame=tk.Frame(frame_flow_right, background=backs[widget_no], height=120, width=120)
    parent_frame.grid(row=0, column=widget_no, padx=5)

    label=tk.Label(parent_frame, text='Total\nRooms', background=backs[widget_no], foreground='white')
    label.pack(pady=(10,0), padx=12, fill=tk.BOTH)
    label['font']=h2_font

    label_av_rooms=tk.Label(parent_frame, text=availableRooms('t'), background=backs[widget_no], foreground='white')
    label_av_rooms.pack(fill=tk.BOTH)
    label_av_rooms['font']=h1_font

    widget_no+=1

    # Total Money box
    parent_frame=tk.Frame(frame_flow_right, background=backs[widget_no], height=120, width=120)
    parent_frame.grid(row=0, column=widget_no, padx=5)

    label=tk.Label(parent_frame, text='Total Money\nRecieved', background=backs[widget_no], foreground='white')
    label.pack(pady=(10,0), padx=12, fill=tk.BOTH)
    label['font']=h2_font

    label_av_rooms=tk.Label(parent_frame, text="₹"+totalValue(), background=backs[widget_no], foreground='white')
    label_av_rooms.pack(fill=tk.BOTH)
    label_av_rooms['font']=h1_font

    widget_no+=1

    # Full Hotel Value box
    parent_frame=tk.Frame(frame_flow_right, background=backs[widget_no], height=120, width=120)
    parent_frame.grid(row=0, column=widget_no, padx=5)

    label=tk.Label(parent_frame, text='Full Hotel\nValue', background=backs[widget_no], foreground='white')
    label.pack(pady=(10,0), padx=12, fill=tk.BOTH)
    label['font']=h2_font

    label_av_rooms=tk.Label(parent_frame, text='₹'+totalValue(), background=backs[widget_no], foreground='white')
    label_av_rooms.pack(fill=tk.BOTH)
    label_av_rooms['font']=h1_font

    widget_no+=1

    # Available rooms box
    parent_frame=tk.Frame(frame_flow_right, background=backs[widget_no], height=120, width=120)
    parent_frame.grid(row=0, column=widget_no, padx=5)

    label=tk.Label(parent_frame, text='Vacant\nRooms', background=backs[widget_no], foreground='white')
    label.pack(pady=(10,0), padx=12, fill=tk.BOTH)
    label['font']=h2_font

    label_av_rooms=tk.Label(parent_frame, text=availableRooms(), background=backs[widget_no], foreground='white')
    label_av_rooms.pack(fill=tk.BOTH)
    label_av_rooms['font']=h1_font

    widget_no+=1

    """ # ---Reserve---
    frame_reserve=tk.Frame(frame_main)
    frame_reserve.place(x=0, y=0, width=670, height=400)


    # ---Rooms---
    frame_rooms=tk.Frame(frame_main)
    frame_rooms.place(x=0, y=0, width=670, height=400)


    # ---Payment---
    frame_payment=tk.Frame(frame_main)
    frame_payment.place(x=0, y=0, width=670, height=400)


    # ---Account---
    frame_account=tk.Frame(frame_main)
    frame_account.place(x=0, y=0, width=670, height=400) """

    # Should be at end of function
    #home() # For placing side panel and bringing dashboard to front
    

# Globally accessed variables across main.py
sec_ques=("What was the first movie you watched at the cinema?",
    "Where were you born?",
    "What was the name of your first pet?",
    "What is your favourite dish?",
    "What brand was your first car of?",
    "what is your favourite movie?",
    "What is your favourite colour?")

acceptables=(*[chr(i) for i in range(97,123)], "_",*[str(i) for i in range(10)], ".")

# Main window constructor
root = tk.Tk()
root.withdraw()
loginWindow()
root.mainloop()