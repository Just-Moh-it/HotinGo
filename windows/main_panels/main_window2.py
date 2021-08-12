from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
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
import windows

class MainWindow2(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Hotel Management System")
        self.main_window_config = config.get('windows').get('main_window')
        self.geometry("".join((str(self.main_window_config.get('win_width')), "x", str(self.main_window_config.get('win_height')), "+300+200")))
        self.grid_propagate(False)

        # ---Users---
        self.user = kwargs.get('user') or 'admin'

        # These frames are to be put in the main window
        self.frames_to_show = [
            Dashboard,
            Reserve,
            Rooms,
            Account,
            Payment
        ]

        # Root Window
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)


        # --------------Work Frames and controls------------------
        # ---Header Container---
        self.header_container=tk.Frame(self, width=630, height=40, pady=10)
        self.header_container.grid(row=0, column=0)
        self.header_container.grid_columnconfigure(0, weight=1)

        # Frame_name Header
        info_header=tk.Label(self.header_container, text="Hotel Management System", font=fonts.get('h1'), justify=tk.LEFT)
        info_header.grid(row=0, column=0, sticky=tk.W, columnspan=3)

        login_status=tk.Label(self.header_container, text="Logged in as: " + self.user, justify=tk.RIGHT)
        login_status.grid(row=0, column=4, sticky=tk.E)

        # ------------Main/Content-Panel------------------
        self.main_panel = ttk.Notebook(self)
        self.main_panel.grid(row=1, column=0)
        # self.main_panel.grid_propagate(False)

        # ------- Adding Buttons and Respective Panels -----------
        self.frames = {}
        for i, F in enumerate(self.frames_to_show):

            # # Button in navbar
            # button = tk.Button(self.nav_bar, text=F.__name__, relief=tk.FLAT, command=lambda x = F.__name__: self.show_frame(x))
            # button.grid(row=i + 1, column=0, sticky="ew", padx=10, pady=10)


            # Panel in Main Window
            frame = F(self.main_panel, self, width=780, height=300)
            self.main_panel.add(frame, text=F.__name__)
            self.frames[F.__name__] = frame


        # # ---Navigation Frame---
        # frame_navigation=tk.Frame(main, background='white')
        # frame_navigation.place(x=0, y=0, width=nav_width, height=win_height)

        # #---Main Frame---
        # self=tk.Frame(main, background='white')
        # self.place(x=170, y=0, width=win_width-nav_width, height=win_height)

        # # Header : Navigation
        # header_main=tk.Label(frame_navigation, text="Hotel\nManagement\nSystem", background='white')
        # header_main.pack(fill=tk.X, pady=(30,0))
        # header_main['font']=fonts.get('h1')

        # # Nav-Selected Pane-Panel
        # panel_side=tk.Frame(frame_navigation, background='#c32148', height=32, width=5)
        # panel_side.place(x=0,y=0)

        # ---Footer Container---
        self.footer_container=tk.Frame(self, width=630, height=40, pady=10)
        self.footer_container.grid(row=2, column=0)

        logout = tk.Button(self.footer_container, text="Logout", command=self.logout)
        logout.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        print("Raised", page_name)
        # print(self.frames)
        frame = self.frames[page_name]
        print(frame)
        frame.tkraise()


# def mainWindow():

#     # -----------Constructor------------------
#     main=tk.Tk()
#     main.title("Main-Hotel Management System")
#     main.geometry("".join((str(win_width), "x", str(win_height), "+300+200")))
#     main.grid_propagate(False)

#     global user # Preserve user var b/w login and main window
#     # For testing purposes only. Remove in final build to reduce unauthorized access

    def logout(self):
        confirm=messagebox.askyesno('Confirm log-out', "Do you really want to log out?")
        if confirm==True:
            user=None
            login.loginWindow()
            self.destroy()


#     # ---Reserve---
#     frame_reserve=Reserve(self)

#     # ---Rooms---
#     frame_rooms=Rooms(self)


#     # ---Payment---
#     frame_payment=Payment(self)


#     # ---Account---
#     frame_account=Account(self)


#     # ---Dashboard---
#     frame_dashboard=Dashboard(self)

#     def startup():
#         # Follow these commands on startup
#         timer = threading.Timer(60.0, dashboard)
#         timer.start



    """
        # Should be at end of function
        #dashboard() # For placing side panel and bringing dashboard to front
    """

