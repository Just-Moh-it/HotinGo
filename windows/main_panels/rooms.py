import tkinter as tk
from config import fonts
import controller

class Rooms(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # self.controller = parent.controller
        self.parent = parent


        # ------ State Handling -----
        # Form fields and variables

        # Form for containing all the data
        self.data = {'room_no': '', 'price': '', 'room_type': ''}

        for label in self.data.keys():
            self.data[label] = tk.StringVar()

        # Form for displaying the data

        # heading = tk.Label(self.root, "Add")
        # heading.grid(row=0, column=0)
        tk.Label(self, font=fonts.get('h2'), text='Add a room').grid(row=0, column=0, pady=3, sticky='nsew')


        # ----- Form Fields -----
        # Room Number
        tk.Label(self, text='Room Number').grid(row=1, column=0, sticky='e')
        self.data['room_no'] = tk.Entry(self)
        self.data['room_no'].grid(row=1, column=5, sticky='w')
        self.data['room_no'].focus_set()

        # Price
        tk.Label(self, text='Price (inr per night)').grid(row=2, column=0, sticky='e')
        self.data['price'] = tk.Entry(self, textvariable=self.data['price'])
        self.data['price'].grid(row=2, column=1, sticky='w')

        # Type
        tk.Label(self, text='Room Type').grid(row=3, column=0, sticky='e')
        self.data['room_type'] = tk.Entry(self, textvariable=self.data['room_type'])
        self.data['room_type'].grid(row=3, column=1, sticky='w')

        # ----- Form Buttons -----
        # Save
        tk.Button(self, text='Save', command=self.save).grid(row=5, column=0, sticky='e')
        # Cancel
        tk.Button(self, text='Cancel', command=self.reset).grid(row=5, column=1, sticky='w')

    # Save the data to the database
    def save(self):
        # print all the fields
        print([value.get() for _, value in self.data.items()])
        # check if any fields are empty
        for label in self.data.keys():
            if self.data[label].get() == '':
                tk.messagebox.showinfo('Error', 'Please fill in all the fields')
                return

        # Save the room




    # Reset the form
    def reset(self):
        self.controller.show_frame('Add_Room')
