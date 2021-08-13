import tkinter as tk
import tkinter.ttk as ttk
from config import fonts
import controller
import controller as db_controller

class Guests(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        # self.controller = parent.controller
        self.parent = parent

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ShowGuests, AddGuest):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("ShowGuests")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class ShowGuests(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.controller = controller

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky="nsew")

        # Add heading label
        self.heading = tk.Label(self.container, text="Guests", font=fonts.get('h2'))
        self.heading.grid(row=0, column=0, sticky="nsew", columnspan=2)


        # Create a treeview with guests as columns and fetch data from the database
        self.tree = ttk.Treeview(self.container, height=20)
        self.guests = ttk.Treeview(self.container)
        self.guests['columns']=('Id', 'Name', 'Address', 'Email', 'Phone', 'City', 'Created At')

        # Shorten the firls column
        self.guests.column('#0', width=0, stretch=tk.NO)
        for col in self.guests['columns']:
            self.guests.column(col, anchor=tk.CENTER, width=80)
            self.guests.heading(col, text=col, anchor=tk.CENTER)

        #  Add data to the treeview
        self.refresh()
        # Place the TreeView
        self.guests.grid(row=1, column=0)

        # Switch pages button
        tk.Button(self.container, text="Add Guest", command=lambda: controller.show_frame("AddGuest")).grid(row=2, column=0, sticky="w")
        tk.Button(self.container, text="Refresh", command=self.refresh).grid(row=2, column=1, sticky="w")

    def refresh(self):
        # Clear previous entries
        # for row in self.tree.get_children():
        #     self.tree.delete(row)
        #     self.update()
        # Clear treeview
        self.guests.delete(*self.guests.get_children())
        print("refreshed")

        # Fetch data from the database and add them to the treeview
        self.guests_data = db_controller.get_guests()
        if self.guests_data:
            for guest in self.guests_data:
                self.guests.insert('', 'end', values=guest)



class AddGuest(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # ------ State Handling -----
        # Form fields and variables

        # Form for containing all the data
        self.data = {'name': '', 'address': '', 'email': '', 'city': '', 'phone': ''}

        for label in self.data.keys():
            self.data[label] = tk.StringVar()

        # Form for displaying the data

        # heading = tk.Label(self.root, "Add")
        # heading.grid(row=0, column=0)
        tk.Label(self, font=fonts.get('h2'), text='Add a guest').grid(row=0, column=0, pady=3, sticky='nsew')

        # ----- Form Fields -----
        # form container
        self.form_container = tk.Frame(self)
        self.form_container.grid(row=1, column=0, sticky="nsew")

        for i, field in enumerate(self.data.keys()):
            tk.Label(self.form_container, text=field.capitalize()).grid(row=i+1, column=0, sticky='nsew')
            self.data[field] = tk.Entry(self.form_container)
            self.data[field].grid(row=i+1, column=1, sticky='nsew')

        # ----- Form Buttons -----
        # Save
        tk.Button(self, text='Save', command=self.save).grid(row=2, column=0, sticky='e')

        tk.Button(self, text="Cancel", command=lambda: controller.show_frame("ShowGuests")).grid(row=2, column=1, sticky='e')

    # Save the data to the database
    def save(self):
        # print all the fields
        print([value.get() for value in self.data.values()])
        # check if any fields are empty
        for label in self.data.keys():
            if self.data[label].get() == '':
                tk.messagebox.showinfo('Error', 'Please fill in all the fields')
                return

        # Save the guest
        result = controller.add_guest(*[self.data[label].get() for label in ('name', 'address', 'city', 'email', 'phone')])

        if result:
            tk.messagebox.showinfo('Success', 'Guest added successfully')
            self.controller.show_frame("ShowGuests")
        else:
            tk.messagebox.showerror('Error', 'Unable to add guest. Please make sure the data is validated')




