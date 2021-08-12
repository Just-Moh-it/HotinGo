import tkinter as tk
from config import fonts

class Account(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        tk.Label(self, font=fonts.get('h2'), text='Account').grid(row=0, column=0, pady=3, sticky='nsew')

        statistics_container=tk.Frame(self)
        statistics_container.grid(row=1, column=0)
