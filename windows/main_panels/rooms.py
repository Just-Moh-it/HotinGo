import tkinter as tk
import tkinter.ttk as ttk
from config import fonts
import controller
import controller as db_controller

class Rooms(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # self.controller = parent.controller
        self.parent = parent

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ShowRooms, AddRoom):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ShowRooms")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class ShowRooms(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.controller = controller

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        # Add heading label
        self.heading = tk.Label(self.container, text="Rooms", font=fonts.get('h2'))
        self.heading.grid(row=0, column=0, sticky="nsew", columnspan=2)


        # Create a treeview with rooms as columns and fetch data from the database
        self.tree = ttk.Treeview(self.container, height=20)
        self.rooms = ttk.Treeview(self.container)
        self.rooms['columns']=('Id', 'Number', 'Price', 'Type', 'Created At')

        # Shorten the firls column
        self.rooms.column('#0', width=0, stretch=tk.NO)
        for col in self.rooms['columns']:
            self.rooms.column(col, anchor=tk.CENTER, width=80)
            self.rooms.heading(col, text=col, anchor=tk.CENTER)

        #  Add data to the treeview
        self.refresh()
        # Place the TreeView
        self.rooms.grid(row=1, column=0)

        # Switch pages button
        tk.Button(self.container, text="Add Room", command=lambda: controller.show_frame("AddRoom")).grid(row=2, column=0, sticky="w")
        tk.Button(self.container, text="Refresh", command=self.refresh).grid(row=2, column=1, sticky="w")

    def refresh(self):
        # Clear previous entries
        # for row in self.tree.get_children():
        #     self.tree.delete(row)
        #     self.update()
        # Clear treeview
        self.rooms.delete(*self.rooms.get_children())
        print("refreshed")

        # Fetch data from the database and add them to the treeview
        self.rooms_data = db_controller.get_rooms()
        if self.rooms_data:
            for room in self.rooms_data:
                self.rooms.insert('', 'end', values=room)



class AddRoom(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)
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
        # Room Number
        tk.Label(self, text='Room Number').grid(row=1, column=0, sticky='e')
        self.data['room_no'] = tk.Entry(self)
        self.data['room_no'].grid(row=1, column=1, sticky='w')
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

        tk.Button(self, text="Cancel", command=lambda: controller.show_frame("ShowRooms")).grid(row=5, column=1, sticky='e')

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
        result = controller.add_room(self.data['room_no'].get(), self.data['price'].get(), self.data['room_type'].get())

        if result:
            tk.messagebox.showinfo('Success', 'Room added successfully')
            self.controller.show_frame("ShowRooms")
        else:
            tk.messagebox.showerror('Error', 'Unable to add room. Please make sure the data is validated')




