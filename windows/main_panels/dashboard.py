import tkinter as tk
from config import fonts

class Dashboard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.pack(expand=True, fill=tk.BOTH)

        tk.Label(self, font=fonts.get('h2'), text='Statistics').grid(row=0, column=0, pady=3, sticky='w')

        statistics_container=tk.Frame(self)
        statistics_container.grid(row=1, column=0)

        widget_no=0 # For keeping track of no. of widgets made

        # initializing Variables
        # Todo: make this dynamic
        label_va_rooms = "0";
        label_bo_rooms = "2";
        label_to_rooms = "0";
        label_to_money = "0";
        label_fu_hotel = "0";
        label_temp = "0";

        boxes = [
            {
                'name': 'Vacant\nRooms',
                'val-label': label_va_rooms,
                'bg': '#FF0013'
            },
            {
                'name': 'Booked\nRooms',
                'val-label': label_bo_rooms,
                'bg': '#FF9100'
            },
            {
                'name': 'Total\nRooms',
                'val-label': label_to_rooms,
                'bg': '#FFC200'
            },
            {
                'name': 'Total Money\nRecieved',
                'val-label': label_va_rooms,
                'bg': '#00B950'
            },
            {
                'name': 'Full Hotel\nValue',
                'val-label': label_fu_hotel,
                'bg': '#4842B8'
            },
            {
                'name': 'Temp\nValue',
                'val-label': label_temp,
                'bg': '#AD00B1'
            }
        ]

        for widget_no, box in enumerate(boxes):
            '''
                Adding widgets from it's dictionary
            '''
            # Available rooms box
            parent_frame=tk.Frame(statistics_container, background=box.get('bg'), height=120, width=120)
            parent_frame.grid(row=0, column=widget_no, padx=5)

            label=tk.Label(parent_frame, text=box.get('name'), background=box.get('bg'), foreground='white')
            label.pack(pady=(10,0), padx=12, fill=tk.BOTH)
            label['font']=fonts.get('h3')

            labll=tk.Label(parent_frame, text=box.get('val-label'), background=box.get('bg'), foreground='white')
            labll.pack(fill=tk.BOTH)
            labll['font']=fonts.get('h1')
