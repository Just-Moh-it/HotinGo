from pathlib import Path

from tkinter import Frame, Canvas, Entry, Text, Button, PhotoImage, messagebox
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def add_reservations():
    AddReservations()


class AddReservations(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.data = {"g_id": "", "check_in": "", "meal": "", "r_id": ""}

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
        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(137.5, 153.0, image=self.entry_image_1)

        self.canvas.create_text(
            52.0,
            128.0,
            anchor="nw",
            text="Guest Id",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(141.5, 165.0, image=self.entry_image_2)
        entry_2 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        entry_2.place(x=52.0, y=153.0, width=179.0, height=22.0)
        self.data["g_id"] = entry_2

        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(137.5, 259.0, image=self.entry_image_3)

        self.canvas.create_text(
            52.0,
            234.0,
            anchor="nw",
            text="Is Taking Meal",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(141.5, 271.0, image=self.entry_image_4)
        entry_4 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        entry_4.place(x=52.0, y=259.0, width=179.0, height=22.0)
        self.data["r_id"] = entry_4

        self.entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(378.5, 153.0, image=self.entry_image_5)

        self.canvas.create_text(
            293.0,
            128.0,
            anchor="nw",
            text="Room Id",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(382.5, 165.0, image=self.entry_image_6)
        entry_6 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            foreground="#777777",
            font=("Montserrat Bold", 18 * -1),
        )
        entry_6.place(x=293.0, y=153.0, width=179.0, height=22.0)
        self.data["meal"] = entry_6

        self.entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(378.5, 259.0, image=self.entry_image_7)

        self.canvas.create_text(
            293.0,
            234.0,
            anchor="nw",
            text="Check-in Time",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
        entry_bg_8 = self.canvas.create_image(382.5, 271.0, image=self.entry_image_8)
        entry_8 = Entry(
            self,
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            foreground="#777777",
            font=("Montserrat Bold", 18 * -1),
        )
        entry_8.place(x=293.0, y=259.0, width=179.0, height=22.0)
        self.data["check_in"] = entry_8

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.save,
            relief="flat",
        )
        button_1.place(x=164.0, y=322.0, width=190.0, height=48.0)

        self.canvas.create_text(
            139.0,
            59.0,
            anchor="nw",
            text="Add a Reservation",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            549.0,
            59.0,
            anchor="nw",
            text="Operations",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_rectangle(
            515.0, 59.0, 517.0, 370.0, fill="#EFEFEF", outline=""
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("view"),
            relief="flat",
        )
        button_2.place(x=547.0, y=116.0, width=209.0, height=74.0)

        self.button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
        button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("edit"),
            relief="flat",
        )
        button_3.place(x=547.0, y=210.0, width=209.0, height=74.0)
        # Set default value for entry
        self.data["check_in"].insert(0, "now")

    # Save the data to the database
    def save(self):
        # check if any fields are empty
        for label in self.data.keys():
            if self.data[label].get() == "":
                messagebox.showinfo("Error", "Please fill in all the fields")
                return

        # Save the reservation
        result = db_controller.add_reservation(
            *[self.data[label].get() for label in ("g_id", "meal", "r_id", "check_in")]
        )

        if result:
            messagebox.showinfo("Success", "Reservation added successfully")
            self.parent.navigate("view")
            self.parent.refresh_entries()

            # clear all fields
            for label in self.data.keys():
                self.data[label].delete(0, "end")
        else:
            messagebox.showerror(
                "Error",
                "Unable to add reservation. Please make sure the data is validated",
            )
