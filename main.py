import tkinter as tk
from windows.login import loginWindow
from windows.main_panels.main_window import MainWindow
from windows.main_panels.main_window2 import MainWindow2

# Main window constructor
root = tk.Tk() # Make temporary window for app to start
root.withdraw() # WithDraw the window


if (__name__ == "__main__"):

    # loginWindow()
    MainWindow2()

    root.mainloop()