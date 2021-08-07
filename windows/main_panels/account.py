import tkinter as tk
from config import fonts

class Account:
    def __init__(self, root) -> None:
        # ---Account---
        frame_account=tk.Frame(root)
        frame_account.place(x=0, y=0, width=670, height=400)