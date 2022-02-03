from pathlib import Path

from tkinter import (
    Frame,
    Canvas,
    Entry,
    Label,
    Text,
    Button,
    PhotoImage,
    messagebox,
    StringVar,
    IntVar,
)
import controller as db_controller

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def update_rooms():
    UpdateRooms()


class UpdateRooms(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_r_id = self.parent.selected_rid

        self.configure(bg="#FFFFFF")

        self.data = {
            "id": StringVar(),
            "number": StringVar(),
            "type": StringVar(),
            "price": IntVar(),
        }

        self.initialize()

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
        self.canvas.create_rectangle(
            40.0, 14.0, 742.0, 16.0, fill="#EFEFEF", outline=""
        )

        self.canvas.create_text(
            116.0,
            33.0,
            anchor="nw",
            text="Update Room",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            116.0,
            65.0,
            anchor="nw",
            text="Change Details",
            fill="#808080",
            font=("Montserrat SemiBold", 16 * -1),
        )

        self.button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.parent.navigate("add"),
            relief="flat",
        )
        button_1.place(x=40.0, y=33.0, width=53.0, height=53.0)

        self.image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(206.0, 170.0, image=self.image_image_1)

        self.canvas.create_text(
            71.56398010253906,
            145.0,
            anchor="nw",
            text="Room ID",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.id_text = self.canvas.create_text(
            72.0,
            172.0,
            anchor="nw",
            text="1024",
            fill="#777777",
            font=("Montserrat SemiBold", 17 * -1),
        )

        self.image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(206.0, 276.0, image=self.image_image_2)

        self.canvas.create_text(
            71.56398010253906,
            251.0,
            anchor="nw",
            text="Room Type",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            212.8127899169922, 288.0, image=self.entry_image_1
        )
        entry_1 = Entry(
            self,
            font=("Montserrat Bold", 18 * -1),
            textvariable=self.data["type"],
            foreground="#777777",
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
        )
        entry_1.place(
            x=71.56398010253906, y=276.0, width=282.49761962890625, height=22.0
        )

        self.image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(583.0, 170.0, image=self.image_image_3)

        self.canvas.create_text(
            455.0473937988281,
            145.0,
            anchor="nw",
            text="Room Number",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(589.5, 182.0, image=self.entry_image_2)
        entry_2 = Entry(
            self,
            font=("Montserrat Bold", 18 * -1),
            textvariable=self.data["number"],
            foreground="#777777",
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
        )
        entry_2.place(x=455.0, y=170.0, width=269.0, height=22.0)

        self.image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(583.0, 278.0, image=self.image_image_4)

        self.canvas.create_text(
            455.0473937988281,
            253.0,
            anchor="nw",
            text="Price",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            589.5094757080078, 290.0, image=self.entry_image_3
        )
        entry_3 = Entry(
            self,
            font=("Montserrat Bold", 18 * -1),
            textvariable=self.data["price"],
            foreground="#777777",
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
        )
        entry_3.place(
            x=455.0473937988281, y=278.0, width=268.9241638183594, height=22.0
        )

        self.button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
        button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.handle_update,
            relief="flat",
        )
        button_2.place(x=326.0, y=339.0, width=144.0, height=48.0)

    def initialize(self):
        self.selected_r_id = self.parent.selected_rid
        self.rooms_data = self.parent.room_data

        # Filter out all reservations for selected id reservation
        self.selected_rooms_data = list(
            filter(lambda x: str(x[0]) == self.selected_r_id, self.rooms_data)
        )

        if self.selected_rooms_data:
            self.selected_rooms_data = self.selected_rooms_data[0]

            self.canvas.itemconfigure(self.id_text, text=self.selected_rooms_data[0])
            self.data["number"].set(self.selected_rooms_data[1])
            self.data["type"].set(self.selected_rooms_data[2])
            self.data["price"].set(self.selected_rooms_data[3])

    def handle_update(self):
        result = db_controller.update_rooms(
            self.selected_r_id,
            room_no=self.data["number"].get(),
            room_type=self.data["type"].get(),
            price=self.data["price"].get(),
        )

        if result:
            messagebox.showinfo("Successful", "Details updated successfully")
            self.parent.navigate("view")
            self.parent.windows.get("view").handle_refresh()
            # clear all fields
            for label in self.data.keys():
                self.data[label].set("")
            self.parent.windows['view'].handle_refresh()
        else:
            messagebox.showerror("Error", "Failed to update details")
