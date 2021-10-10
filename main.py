import tkinter as tk
from new_gui.login.gui import loginWindow
# from windows.main_panels.main_window import MainWindow

# Main window constructor
root = tk.Tk() # Make temporary window for app to start
root.withdraw() # WithDraw the window


if (__name__ == "__main__"):

    loginWindow()
    # MainWindow()

    root.mainloop()
