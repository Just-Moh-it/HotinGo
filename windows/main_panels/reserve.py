import tkinter as tk
from config import fonts

class Reserve:
    def __init__(self, root) -> None:
        # ---Reserve---
        frame_reserve=tk.Frame(root)
        frame_reserve.place(x=0, y=0, width=670, height=400)