from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def update_reservations():
    UpdateReservations()

class UpdateReservations(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        # self.controller = parent.controller
        self.parent = parent

        # self.geometry("797x432")
        self.configure(bg = "#FFFFFF")


        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 432,
            width = 797,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            40.0,
            14.0,
            742.0,
            16.0,
            fill="#EFEFEF",
            outline="")

        self.canvas.create_text(
            116.0,
            33.0,
            anchor="nw",
            text="Update Reservation",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            116.0,
            65.0,
            anchor="nw",
            text="Change Details",
            fill="#808080",
            font=("Montserrat SemiBold", 16 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate('add'),
            relief="flat"
        )
        button_1.place(
            x=40.0,
            y=33.0,
            width=53.0,
            height=53.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            145.0,
            150.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            60.0,
            125.0,
            anchor="nw",
            text="Reservation ID",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.canvas.create_text(
            60.0,
            152.0,
            anchor="nw",
            text=self.parent.selected_r_id,
            fill="#979797",
            font=("Montserrat Bold", 18 * -1)
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            145.0,
            246.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            60.0,
            221.0,
            anchor="nw",
            text="Is Taking Meal",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            149.5,
            258.0,
            image=self.entry_image_1
        )
        entry_2 = Entry(self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777"
        )
        entry_2.place(
            x=60.0,
            y=246.0,
            width=179.0,
            height=22.0
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            145.0,
            342.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            60.0,
            317.0,
            anchor="nw",
            text="Type",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            149.5,
            354.0,
            image=self.entry_image_2
        )
        entry_2 = Entry(self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777"
        )
        entry_2.place(
            x=60.0,
            y=342.0,
            width=179.0,
            height=22.0
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            391.0,
            150.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            306.0,
            125.0,
            anchor="nw",
            text="Guest Id",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_3 = self.canvas.create_image(
            395.5,
            162.0,
            image=self.entry_image_3
        )
        entry_2 = Entry(self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777"
        )
        entry_2.place(
            x=306.0,
            y=150.0,
            width=179.0,
            height=22.0
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            391.0,
            246.0,
            image=self.image_image_5
        )

        self.canvas.create_text(
            306.0,
            221.0,
            anchor="nw",
            text="Check-in Time",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_4 = self.canvas.create_image(
            395.5,
            258.0,
            image=self.entry_image_4
        )
        entry_2 = Entry(self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777"
        )
        entry_2.place(
            x=306.0,
            y=246.0,
            width=179.0,
            height=22.0
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            391.0,
            342.0,
            image=self.image_image_6
        )

        self.canvas.create_text(
            306.0,
            317.0,
            anchor="nw",
            text="Reservation Date",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_5 = self.canvas.create_image(
            395.5,
            354.0,
            image=self.entry_image_5
        )
        entry_2 = Entry(self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777"
        )
        entry_2.place(
            x=306.0,
            y=342.0,
            width=179.0,
            height=22.0
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        image_7 = self.canvas.create_image(
            637.0,
            150.0,
            image=self.image_image_7
        )

        self.canvas.create_text(
            552.0,
            125.0,
            anchor="nw",
            text="Room Id",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.entry_image_6 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_6 = self.canvas.create_image(
            641.5,
            162.0,
            image=self.entry_image_6
        )
        entry_2 = Entry(self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777"
        )
        entry_2.place(
            x=552.0,
            y=150.0,
            width=179.0,
            height=22.0
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        image_8 = self.canvas.create_image(
            637.0,
            246.0,
            image=self.image_image_8
        )

        self.canvas.create_text(
            552.0,
            221.0,
            anchor="nw",
            text="Check Out Time",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1)
        )

        self.entry_image_7 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_7 = self.canvas.create_image(
            641.5,
            258.0,
            image=self.entry_image_7
        )
        entry_2 = Entry(self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777"
        )
        entry_2.place(
            x=552.0,
            y=246.0,
            width=179.0,
            height=22.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(
            x=570.0,
            y=318.0,
            width=144.0,
            height=48.0
        )
