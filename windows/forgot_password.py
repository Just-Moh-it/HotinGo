'''
    Sadly had to let this feature go
'''
# from tkinter import messagebox
# import tkinter as tk
# from config import fonts
# from . import login
# from config import config
# from controller import *

# def forgotPwdWindow():

#     def loginBtn():
#         forgot_pwd.destroy()
#         login.loginWindow()

#     def changePwd():
#         if not checkUser(username.get()):
#             messagebox.showerror("Invalid username", "Please enter a valid username"); return
#         elif 30<len(password.get())<8 or password.get().isspace():
#             messagebox.showerror("Invalid-HMS", printer("Please enter a valid 'Password'. Passwords must", ['• Contain 8 characters or more', "\n\t• Not be empty"]))
#             username_tb.focus(); return

#         if True or updatePassword(username.get().lower(), sec_ans.get(), sec_que.get(), password.get()):
#             login=messagebox.askyesno("Successful", "Password Changed successfully. Proceed to login?")
#             if login==True:
#                 loginBtn(); return
#         else:
#             messagebox.showerror("Error", "Record with the following details not found."); return


#     # ------------Constructor--------------
#     forgot_pwd=tk.Tk()
#     forgot_pwd.title("Reset Password-Hotel Management System")
#     forgot_pwd.geometry("535x240+450+285")
#     forgot_pwd.resizable(0,0)
#     forgot_pwd['background']='white'

#     # Main Frame
#     frame_forgot_pwd=tk.Frame(forgot_pwd, background='white')
#     frame_forgot_pwd.place(x=20, y=25)

#     # Heading
#     tk.Label(frame_forgot_pwd, text="Reset Password", font=fonts.get('h1')).grid(row=0, column=0, columnspan=2, padx=(60,0))

#     # Username tb
#     tk.Label(frame_forgot_pwd, text="Username").grid(row=1, column=0)

#     username=tk.StringVar(forgot_pwd)
#     username_tb=tk.Entry(frame_forgot_pwd, textvariable=username, width=40)
#     username_tb.grid(row=1, column=1)

#     # Security Questions cb
#     tk.Label(frame_forgot_pwd, text="Security Question").grid(row=2, column=0)

#     sec_que=tk.StringVar(forgot_pwd)
#     sec_que.set(config.get('SEC_QUES')[0])
#     sec_que_cb=tk.OptionMenu(frame_forgot_pwd, sec_que, *config.get('SEC_QUES'))
#     sec_que_cb['width']=38
#     sec_que_cb.grid(row=2, column=1)

#     # Password tb
#     tk.Label(frame_forgot_pwd, text="Security Answer").grid(row=3, column=0)

#     sec_ans=tk.StringVar(forgot_pwd)
#     sec_ans_tb= tk.Entry(frame_forgot_pwd, textvariable=sec_ans, width=40)
#     sec_ans_tb.grid(row=3, column=1)

#     # Password tb
#     tk.Label(frame_forgot_pwd, text="Set New Pasword").grid(row=4, column=0)

#     password=tk.StringVar(forgot_pwd)
#     password_tb=tk.Entry(frame_forgot_pwd, textvariable=password, width=40)
#     password_tb.grid(row=4, column=1)

#     offset=60

#     # Change Password Button
#     change_pwd_button=tk.Button(frame_forgot_pwd, text="Change\nPassword", height=2, width=12, command=lambda : changePwd())
#     change_pwd_button.grid(row=5, column=0, columnspan=2, pady=10, padx=(0,120-offset))

#     # Login Button
#     login_button=tk.Button(frame_forgot_pwd, text="Login", height=2, width=12, command=loginBtn)
#     login_button.grid(row=5, column=0, columnspan=2, pady=10, padx=(120+offset,0))
