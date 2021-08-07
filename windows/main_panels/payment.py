import tkinter as tk
from config import fonts

class Payment:
    def __init__(self, root) -> None:
        # ---Payment---
        frame_payment=tk.Frame(root)
        frame_payment.place(x=0, y=0, width=670, height=400)