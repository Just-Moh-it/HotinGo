import tkinter as tk

class Dashboard:
    def __init__(self, root) -> None:
        # ---Dashboard---
        frame_dashboard=tk.Frame(root)
        frame_dashboard.place(x=0, y=40, width=630, height=400)

        boxes=['#FF0013', '#FF9100', '#FFC200', '#00B950', '#0090F7', '#4842B8', '#AD00B1']

        tk.Label(frame_dashboard, font=fonts.get('h2'), text='Statistics').grid(row=0, column=0, pady=3, sticky='w')

        frame_flow_right=tk.Frame(frame_dashboard)
        frame_flow_right.grid(row=1, column=0)

        widget_no=0 # For keeping track of no. of widgets made

        # initializing Variables
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
            parent_frame=tk.Frame(frame_flow_right, background=box.get('bg'), height=120, width=120)
            parent_frame.grid(row=0, column=widget_no, padx=5)

            label=tk.Label(parent_frame, text=box.get('name'), background=box.get('bg'), foreground='white')
            label.pack(pady=(10,0), padx=12, fill=tk.BOTH)
            label['font']=fonts.get('h3')

            labll=tk.Label(parent_frame, text=box.get('val-label'), background=box.get('bg'), foreground='white')
            labll.pack(fill=tk.BOTH)
            labll['font']=fonts.get('h1')

        label_to_money = "5"

if __name__ == '__main__':
    import sys
    # Add the ptdraft folder path to the sys.path list
    sys.path.append('/Users/mohit/programming/hms-updated/')


    # imported at last to avoid circular import error
    from config import fonts

    root = tk.Tk()
    root.title('Dashboard')
    root.geometry('630x400')
    root.resizable(False, False)
    Dashboard(root)
    root.mainloop()
else:
    from config import fonts