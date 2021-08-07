import tkinter as tk
from config import fonts

class Rooms:
    def __init__(self, root) -> None:
        # ---Rooms---
        frame_rooms=tk.Frame(root)
        frame_rooms.place(x=0, y=0, width=670, height=400)