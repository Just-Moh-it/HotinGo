from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def view_reservations():
    ViewReservations()

class ViewReservations(Frame):
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

        self.canvas.create_rectangle(
            40.0,
            342.0,
            742.0,
            344.0,
            fill="#EFEFEF",
            outline="")

        self.canvas.create_text(
            116.0,
            33.0,
            anchor="nw",
            text="View Reservations",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            40.0,
            367.0,
            anchor="nw",
            text="Avail. Actions:",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1)
        )

        self.canvas.create_text(
            116.0,
            65.0,
            anchor="nw",
            text="And Perform Operations",
            fill="#808080",
            font=("Montserrat SemiBold", 16 * -1)
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            666.0,
            59.0,
            image=self.image_image_1
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            680.5,
            60.0,
            image=self.entry_image_1
        )
        entry_1 = Entry(self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            foreground="#777777",
            font=("Montserrat Bold", 18 * -1)
        )
        entry_1.place(
            x=637.0,
            y=48.0,
            width=87.0,
            height=22.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(
            x=525.0,
            y=33.0,
            width=53.0,
            height=53.0
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            617.0,
            60.0,
            image=self.image_image_2
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate('add'),
            relief="flat"
        )
        button_2.place(
            x=40.0,
            y=33.0,
            width=53.0,
            height=53.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(
            x=596.0,
            y=359.0,
            width=146.0,
            height=48.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(
            x=463.0,
            y=359.0,
            width=116.0,
            height=48.0
        )

        self.canvas.create_rectangle(
            40.0,
            101.0,
            742.0,
            329.0,
            fill="#EFEFEF",
            outline="")

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        button_5.place(
            x=272.0,
            y=359.0,
            width=174.0,
            height=48.0
        )
