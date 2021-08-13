import tkinter as tk
from config import fonts

class Rooms(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.controller = controller


        # ------ State Handling -----
        # Form fields and variables

        # Form for containing all the data
        self.data = {'room_no': '', 'price': '', 'room_type': '', '': '', 'room_features': '', 'room_description': ''}

        for label in self.data.keys():
            self.data[label] = tk.StringVar()

        # Form for displaying the data

        # heading = tk.Label(self.root, "Add")
        # heading.grid(row=0, column=0)
        tk.Label(self, font=fonts.get('h2'), text='Add a room').grid(row=0, column=0, pady=3, sticky='nsew')


        # ----- Form Fields -----
        # Name
        tk.Label(self, text='Name:').grid(row=1, column=0, sticky='e')
        self.name = tk.Entry(self)
        self.name.grid(row=1, column=1, sticky='w')
        self.name.focus_set()
        # Description
        tk.Label(self, text='Description:').grid(row=2, column=0, sticky='e')
        self.description = tk.Text(self, height=5, width=40)
        self.description.grid(row=2, column=1, sticky='w')
        # Password
        tk.Label(self, text='Password:').grid(row=3, column=0, sticky='e')
        self.password = tk.Entry(self)
        self.password.grid(row=3, column=1, sticky='w')
        # Password Confirmation

        tk.Label(self, text='Password Confirmation:').grid(row=4, column=0, sticky='e')
        self.password_confirmation = tk.Entry(self)
        self.password_confirmation.grid(row=4, column=1, sticky='w')

        # ----- Form Buttons -----
        # Save
        tk.Button(self, text='Save', command=lambda: print("Not implemented")).grid(row=5, column=0, sticky='e')
        # Cancel
        tk.Button(self, text='Cancel', command=lambda: print("Not implemented").show_frame('MainPanels')).grid(row=5, column=1, sticky='w')
        # Clear
        tk.Button(self, text='Clear', command=lambda: print("Not implemented")).grid(row=5, column=1, sticky='e')
        # Submit
        tk.Button(self, text='Submit', command=lambda: print("Not implemented")).grid(row=5, column=1, sticky='w')
        # Delete
        tk.Button(self, text='Delete', command=lambda: print("Not implemented")).grid(row=5, column=1, sticky='e')

