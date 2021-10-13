from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *

from .add_guests.gui import AddGuests
from .view_guests.main import ViewGuests
from .update_guests.main import UpdateGuests

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def guests():
    Guests()


class Guests(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        # self.controller = parent.controller
        self.parent = parent
        self.selected_rid=None

        # self.geometry("797x432")
        self.configure(bg = "#FFFFFF")

        # Loop through windows and place them
        self.windows = {
            'add': AddGuests(self),
            'view': ViewGuests(self),
            'edit': UpdateGuests(self),
        }

        self.current_window = self.windows['add']
        self.current_window.place(x=0, y=0, width=1013.0,
            height=506.0)

        self.current_window.tkraise()

    def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=1013.0,
            height=506.0)

