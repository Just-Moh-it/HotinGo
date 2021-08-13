import tkinter as tk
from config import fonts


class Rooms(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.controller = controller


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
        # Number
        tk.Label(self, text='Room Number').grid(row=1, column=0, sticky='e')
        self.name = tk.Entry(self, textvariable=self.data['room_no'])
        self.name.grid(row=1, column=1, sticky='w')
        self.name.focus_set()
        # Price
        tk.Label(self, text='Price (inr per night)').grid(row=2, column=0, sticky='e')
        self.price = tk.Entry(self, textvariable=self.data['price'])
        self.price.grid(row=2, column=1, sticky='w')
        # Type
        tk.Label(self, text='Room Type').grid(row=3, column=0, sticky='e')
        self.type = tk.Entry(self, textvariable=self.data['room_type'])
        self.type.grid(row=3, column=1, sticky='w')

        # ----- Form Buttons -----
        # Save
        tk.Button(self, text='Save', command=self.save).grid(row=5, column=0, sticky='e')
        # Cancel
        tk.Button(self, text='Cancel', command=self.reset).grid(row=5, column=1, sticky='w')

    # Save the data to the database
    def save(self):
        # print all the fields
        print([self.data[label].get() for label in self.data.keys()])
        # check if any fields are empty
        for label in self.data.keys():
            if self.data[label].get() == '':
                tk.messagebox.showinfo('Error', 'Please fill in all the fields')
                return

        # Save the room
        self.controller.database.add_room(self.data['room_no'].get(), self.data['price'].get(), self.data['room_type'].get())
        tk.messagebox.showinfo('Success', 'Room added successfully')
        self.reset()


    # Reset the form
    def reset(self):
        self.controller.show_frame('Add_Room')

