import tkinter as tk
from config import fonts

class Reserve(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.controller = controller

        # Form fields and variables

        # Form for containing all the data
        self.data = {}

        for label, value in self.data.items():
            self.data[label] = tk.StringVar()