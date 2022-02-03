from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def about():
    About()


class About(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            36.0,
            43.0,
            anchor="nw",
            text="HotinGo was created by",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(191.0, 26.0, image=self.image_image_1)

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(203.0, 205.0, image=self.image_image_2)

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(565.0, 205.0, image=self.image_image_3)

        self.canvas.create_text(
            56.0,
            121.0,
            anchor="nw",
            text="Tinkerer",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )

        self.canvas.create_text(
            418.0,
            121.0,
            anchor="nw",
            text="SW-Fan",
            fill="#777777",
            font=("Montserrat Medium", 15 * -1),
        )

        self.canvas.create_text(
            56.0,
            138.0,
            anchor="nw",
            text="Mohit",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            418.0,
            138.0,
            anchor="nw",
            text="Anirudh",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            56.0,
            170.0,
            anchor="nw",
            text="Yadav",
            fill="#5E95FF",
            font=("Montserrat Bold", 18 * -1),
        )

        self.canvas.create_text(
            418.0,
            170.0,
            anchor="nw",
            text="Agarwal",
            fill="#5E95FF",
            font=("Montserrat Bold", 18 * -1),
        )

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(308.0, 150.0, image=self.image_image_4)

        self.canvas.create_rectangle(
            56.0, 197.0, 169.0, 199.0, fill="#FFFFFF", outline=""
        )

        self.canvas.create_rectangle(
            418.0, 197.0, 531.0, 199.0, fill="#FFFFFF", outline=""
        )

        self.image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(669.0, 151.0, image=self.image_image_5)

        self.canvas.create_text(
            197.0,
            352.0,
            anchor="nw",
            text="© 2021-22 Mohit and Anirudh, All rights reserved",
            fill="#5E95FF",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            246.0,
            372.0,
            anchor="nw",
            text="Open sourced under the MIT license",
            fill="#5E95FF",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            418.0,
            207.0,
            anchor="nw",
            text="A tech-nerd and a freelance programmer,",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            418.0,
            223.0,
            anchor="nw",
            text="Anirudh likes to kill his time in a world of",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            418.0,
            239.0,
            anchor="nw",
            text="computer. He sometimes can be found in",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            418.0,
            255.0,
            anchor="nw",
            text="the reality, walking his dog or watching",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            418.0,
            271.0,
            anchor="nw",
            text="Star Wars.",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            56.0,
            207.0,
            anchor="nw",
            text="A coding-addict, entusiastic creator, and a",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            56.0,
            223.0,
            anchor="nw",
            text="passionate learner, Mohit likes to bring",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            56.0,
            239.0,
            anchor="nw",
            text="perfection to anything he’s doing. He’s",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            56.0,
            255.0,
            anchor="nw",
            text="also a passionate designer and a die-hard",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )

        self.canvas.create_text(
            56.0,
            271.0,
            anchor="nw",
            text="Avengers fan.",
            fill="#777777",
            font=("Montserrat Medium", 13 * -1),
        )
