from tkinter import messagebox
import tkinter as tk
from helpers import *
from ..forgot_password import *
from .. import login
from tkinter import Misc


# Panel imports
from .dashboard import Dashboard
from .payment import Payment
from .reserve import Reserve
from .rooms import Rooms
from .account import Account

class MainWindow(tk.Tk):


    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Hotel Management System")
        self.main_window_config = config.get('windows').get('main_window')
        self.geometry("".join((str(self.main_window_config.get('win_width')), "x", str(self.main_window_config.get('win_height')), "+300+200")))
        self.grid_propagate(False)
        # These frames are to be put in the main window
        self.frames_to_show = [
            Dashboard,
            Reserve,
            Rooms,
            Account,
            Payment
        ]

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # -----------Navigation-------------------
        self.nav_bar = tk.Frame(container, bg="grey", width=self.main_window_config.get('nav_width'))
        self.nav_bar.grid(row=0, column=0, sticky="nw")

        # ------------Main-Panel------------------
        self.main_panel = tk.Frame(container, bg="grey")
        self.main_panel.grid(row=0, column=1)

        # ------- Adding Buttons and Respective Panels -----------
        self.frames = {}
        for i, F in enumerate(self.frames_to_show):
            def raise_frame():
                self.show_frame(F.__name__)

            # Button in navbar
            button = tk.Button(self.nav_bar, text=F.__name__, relief=tk.FLAT, command=raise_frame)
            button.grid(row=i + 1, column=0, sticky="ew", padx=10, pady=10)


            # Panel in Main Window
            frame = F(self.main_panel, self)
            self.frames[F.__name__] = frame
            frame.pack(expand=True, fill="both")

        # # ---Navigation Frame---
        # frame_navigation=tk.Frame(main, background='white')
        # frame_navigation.place(x=0, y=0, width=nav_width, height=win_height)

        # #---Main Frame---
        # frame_main=tk.Frame(main, background='white')
        # frame_main.place(x=170, y=0, width=win_width-nav_width, height=win_height)

        # # Header : Navigation
        # header_main=tk.Label(frame_navigation, text="Hotel\nManagement\nSystem", background='white')
        # header_main.pack(fill=tk.X, pady=(30,0))
        # header_main['font']=fonts.get('h1')

        # # Nav-Selected Pane-Panel
        # panel_side=tk.Frame(frame_navigation, background='#c32148', height=32, width=5)
        # panel_side.place(x=0,y=0)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        print("Raised", page_name)
        print(self.frames)
        frame = self.frames[page_name]
        frame.tkraise()
# def mainWindow():

#     # -----------Constructor------------------
#     main=tk.Tk()
#     main.title("Main-Hotel Management System")
#     main.geometry("".join((str(win_width), "x", str(win_height), "+300+200")))
#     main.grid_propagate(False)

#     global user # Preserve user var b/w login and main window
#     # For testing purposes only. Remove in final build to reduce unauthorized access
#     """ try: user
#     except NameError: user='admin' """

#     # --------------Tkinter Function--------------

#     def dashboard():
#         panel_side.place(y=button_dashboard.winfo_y()+2)
#         info_header.configure(text='Dashboard')
#     def reserve():
#         panel_side.place(y=button_reserve.winfo_y()+2)
#         info_header.configure(text='Reserve')
#         Misc.tkraise(header_main)
#         print("Hello wolrld")
#     def rooms():
#         panel_side.place(y=button_rooms.winfo_y()+2)
#         info_header.configure(text='Rooms')
#     def payment():
#         panel_side.place(y=button_payment.winfo_y()+2)
#         info_header.configure(text='Payement')
#     def account():
#         panel_side.place(y=button_account.winfo_y()+2)
#         info_header.configure(text='Account')

#     def logout():
#         confirm=messagebox.askyesno('Confirm log-out', "Do you really want to log out?")
#         if confirm==True:
#             user=None
#             login.loginWindow()
#             main.destroy()


#     # ---Navigation Buttons and Title---

#     # Buttons
#     button_dashboard=tk.Button(frame_navigation, text="Dashboard", command=dashboard, height=2, relief=tk.FLAT, background='white')
#     button_dashboard.pack(fill=tk.X, pady=(25,0), padx=(4,0))

#     button_reserve=tk.Button(frame_navigation, text="Reserve", command=reserve, height=2, relief=tk.FLAT, background='white')
#     button_reserve.pack(fill=tk.X, padx=(4,0))

#     button_rooms=tk.Button(frame_navigation, text="Rooms", command=rooms, height=2, relief=tk.FLAT, background='white')
#     button_rooms.pack(fill=tk.X, padx=(4,0))

#     button_payment=tk.Button(frame_navigation, text="Payment", command=payment, height=2, relief=tk.FLAT, background='white')
#     button_payment.pack(fill=tk.X, padx=(4,0))

#     button_account=tk.Button(frame_navigation, text="Account", command=account, height=2, relief=tk.FLAT, background='white')
#     button_account.pack(fill=tk.X, padx=(4,0))

#     button_logout=tk.Button(frame_navigation, text="Log out", command=logout, height=2, relief=tk.FLAT, background='white')
#     button_logout.pack(fill=tk.X, padx=20, pady=(30,0))

#     # Placing sidebar on dashboard
#     panel_side.place(y=134)

#     # --------------Work Frames and controls------------------
#     # ---Top Frame---
#     frame_header=tk.Frame(frame_main, width=630, height=40, pady=10)
#     frame_header.place(x=0, y=0)

#     # Frame_name Header
#     info_header=tk.Label(frame_header, text="Dashboard", font=fonts.get('h1'))
#     info_header.place(x=2)

#     # Logged in as label
#     # !!!!----- To remove in Production ----------
#     try: user
#     except: user='admin'

#     header_main=tk.Label(frame_header, text="Logged in as: " + user, background='white')
#     header_main.place(x=435, y=5)
#     header_main['font']=fonts.get('h2')

#     # ---Reserve---
#     frame_reserve=Reserve(frame_main)

#     # ---Rooms---
#     frame_rooms=Rooms(frame_main)


#     # ---Payment---
#     frame_payment=Payment(frame_main)


#     # ---Account---
#     frame_account=Account(frame_main)


#     # ---Dashboard---
#     frame_dashboard=Dashboard(frame_main)

#     def startup():
#         # Follow these commands on startup
#         timer = threading.Timer(60.0, dashboard)
#         timer.start



    """
        # Should be at end of function
        #dashboard() # For placing side panel and bringing dashboard to front
    """

