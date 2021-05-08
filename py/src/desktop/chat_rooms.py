import tkinter as tk
from functools import partial

import cx_Oracle

from .make_room import MakeRoom
from .window import Window
from core.dao.social_dao import SocialDAO


class ChatRoom(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        # DAO
        this.socialDAO = SocialDAO()

        # ID FOR THE ACTUAL ROOM
        this.akt_room_id = 0

        this.rowconfigure(index=0, weight=1)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=3)


        tk.Label(this, text="Közösségi szobák", font=(None, 25), bg="gray5",fg="snow").grid(row=0, columnspan=2, sticky="NESW")
        # FRAME FOR ROOM NAME
        this.room_frame = tk.LabelFrame(this, text="Szobák", font=(None, 15), width=100, bg="gray5",fg="snow")
        this.room_frame.grid(row=1, column=0, sticky="NESW")

        # FRAME FOR MAIN MESSAGES
        this.main_message_frame = tk.LabelFrame(this, text="Üzenetek", font=(None, 15), bg="gray5",fg="snow", bd=0)
        this.main_message_frame.grid(row=1, column=1, sticky="NESW")
        this.main_message_frame.rowconfigure(index=0, weight=1)
        this.main_message_frame.rowconfigure(index=1, weight=1)
        this.main_message_frame.columnconfigure(index=0, weight=1)

        #CANVAS FOR THE MESSAGES
        this.scroll_message_canvas = tk.Canvas(this.main_message_frame, height=400)
        this.scroll_message_canvas.rowconfigure(index=0, weight=1)
        this.scroll_message_canvas.columnconfigure(index=0, weight=1)
        this.scroll_message_canvas.grid(row=0, column=0, sticky="NESW")
        this.scroll_message_canvas.grid_propagate(False)

        this.scroll_message_scrollbar = tk.Scrollbar(this.main_message_frame,orient="vertical", command=this.scroll_message_canvas.yview)
        this.scroll_message_scrollbar.grid(row=0, column=0, sticky="NES")


        # FRAME FOR MESSAGES
        this.messages_frame = tk.Frame(this.scroll_message_canvas, height=400)
        this.messages_frame.grid(row=0, column=0, sticky="NESW")

        # ADD ROOMS AND MESSAGES FROM DB
        this.room_frame.columnconfigure(index=0, weight=1)
        this.room_frame.columnconfigure(index=1, weight=1)
        this.room_frame.rowconfigure(index=0, weight=1)

        this.member_room = tk.Frame(this.room_frame)
        this.member_room.grid(row=0, column=0, sticky="NESW")

        this.non_member_room = tk.Frame(this.room_frame)
        this.non_member_room.grid(row=0, column=1, sticky="NESW")

        this.load_rooms()

        # MESSAGE WRITER FRAME
        writer_frame = tk.Frame(this.main_message_frame)
        writer_frame.rowconfigure(index=0, weight=1)
        writer_frame.columnconfigure(index=0, weight=3)
        writer_frame.columnconfigure(index=1, weight=1)

        msg_entry = tk.Entry(writer_frame)
        msg_entry.grid(row=0, column=0, sticky="NESW")

        send_button = tk.Button(writer_frame, text="Send",
                                command=partial(this.send_message, msg_entry, data["user"][0]))
        send_button.grid(row=1, column=0, sticky="NESW")

        writer_frame.grid(row=1, column=0, sticky="ESW")

        # BACK BUTTON
        back_button = tk.Button(this, text='Vissza', command=this.go_back)
        back_button.grid(row=2, column=0, sticky="W")

        # MAKE ROOM
        back_button = tk.Button(this, text='Új szoba', command=this.new_room)
        back_button.grid(row=3, column=0, sticky="W")

        this.scroll_message_canvas["bg"] = this["bg"]
        this.messages_frame["bg"] = this["bg"]
        this.room_frame["bg"] = this["bg"]
        this.main_message_frame["bg"] = this["bg"]
        this.non_member_room["bg"] = this["bg"]
        this.member_room["bg"] = this["bg"]
        writer_frame["bg"] = this["bg"]


        this.canvas_win = this.scroll_message_canvas.create_window(0, 0, window=this.messages_frame, anchor=tk.NW)
        this.scroll_message_canvas.config(yscrollcommand=this.scroll_message_scrollbar.set)

        this.messages_frame.bind("<Configure>", this.on_frame_configure)
        this.scroll_message_canvas.bind("<Configure>", this.on_canvas_configure)
        this.scroll_message_canvas.bind_all("<MouseWheel>", this.on_mouse_wheel)


        this.reset()

    def reset(this) -> None:
        this.load_rooms()
        if this.akt_room_id != 0:
            this.to_room(this.akt_room_id)

    def new_room(this):
        this.master.raise_window(MakeRoom)

    def join_room(this, room_id:int) -> None:
        this.socialDAO.insert_to_room(this.data["user"][0], room_id)
        this.load_rooms()

    def load_rooms(this):
        for widget in this.member_room.winfo_children():
            widget.destroy()

        for widget in this.non_member_room.winfo_children():
            widget.destroy()


        tk.Label(this.member_room, text="Szobáim", font=(None, 20), bg="gray5",fg="snow").pack(padx=10, pady=10)
        tk.Label(this.non_member_room, text="Jelentkezés", font=(None, 20), bg="gray5",fg="snow").pack(padx=10, pady=10)

        rooms: list[tuple[int, str]] = this.socialDAO.get_room(this.data["user"][0])
        non_room: list[tuple[int, str]] = this.socialDAO.get_non_member_room(this.data["user"][0])

        for i in range(len(rooms)):
            tk.Button(this.member_room, command=partial(this.to_room, rooms[i][0]), text=rooms[i][1]).pack(fill=tk.X, padx=10, pady=10)

        for i in range(len(non_room)):
            tk.Button(this.non_member_room, command=partial(this.join_room, non_room[i][0]), text=non_room[i][1]).pack(fill=tk.X, padx=10, pady=10)


    def on_frame_configure(this, event) -> None:
        this.scroll_message_canvas.config(scrollregion=this.scroll_message_canvas.bbox("all"))

    def on_canvas_configure(this, event) -> None:
        this.scroll_message_canvas.itemconfig(this.canvas_win, width=event.width)

    def on_mouse_wheel(this, event) -> None:
        if this.scroll_message_canvas.winfo_height() < this.messages_frame.winfo_height():
            this.scroll_message_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    def clean_messages(this) -> None:
        for widget in this.messages_frame.winfo_children():
            widget.destroy()


    def go_back(this) -> None:
        this.master.raise_previous_window()

    def to_room(this, room_id: int) -> None:
        if this.data["user"][4]:
            this.load_messages_admin(room_id)
        else:
            this.load_messages(room_id)

    def send_message(this, content: tk.Entry, user:str):
        this.socialDAO.send_message(user, this.akt_room_id, content.get())
        content.delete(0, "end")
        this.reset()

    def load_messages(this, room_id: int):
        this.clean_messages()
        room_messages = this.socialDAO.get_messages(room_id)
        this.akt_room_id = room_id
        for i in range(len(room_messages)):
            akt_message = tk.Frame(this.messages_frame)
            akt_message.rowconfigure(index=0, weight=1)
            akt_message.columnconfigure(index=0, weight=1)
            akt_message.columnconfigure(index=1, weight=3)
            akt_message.columnconfigure(index=2, weight=1)
            tk.Label(akt_message, text=room_messages[i][0], font=("Ebrima", 18)).grid(row=0, column=0, sticky="W")
            tk.Label(akt_message, text=room_messages[i][3], font=("Ebrima", 15)).grid(row=0, column=1, sticky="WE")
            tk.Label(akt_message, text=room_messages[i][2], font=("Ebrima", 10)).grid(row=0, column=2, sticky="E")
            akt_message.grid(row=i, sticky="W", padx=10, pady=10)

    def load_messages_admin(this, room_id: int):
        this.clean_messages()
        room_messages = this.socialDAO.get_messages(room_id)
        this.akt_room_id = room_id
        for i in range(len(room_messages)):
            akt_message = tk.Frame(this.messages_frame)
            akt_message.rowconfigure(index=0, weight=1)
            akt_message.columnconfigure(index=0, weight=1)
            akt_message.columnconfigure(index=1, weight=3)
            akt_message.columnconfigure(index=2, weight=1)
            akt_message.columnconfigure(index=3, weight=1)
            akt_message.columnconfigure(index=4, weight=1)
            akt_message.columnconfigure(index=5, weight=1)
            tk.Label(akt_message, text=room_messages[i][0], font=("Ebrima", 18)).grid(row=0, column=0, sticky="W")
            tk.Label(akt_message, text=room_messages[i][3], font=("Ebrima", 15)).grid(row=0, column=1, sticky="WE")
            tk.Label(akt_message, text=room_messages[i][2], font=("Ebrima", 10)).grid(row=0, column=2, sticky="E")
            tk.Button(akt_message, text="X", command = partial(this.delete, room_messages[i][0],room_messages[i][2])).grid(row=0, column=3, sticky="W")
            tk.Button(akt_message, text="Módosít", command = partial(this.update_msg,room_messages[i][0],room_messages[i][2],akt_message)).grid(row=0, column=4, sticky="W")
            akt_message.grid(row=i, sticky="W", padx=10, pady=10)

    def delete(this, user:str, date:cx_Oracle.Date) -> None:
        if this.socialDAO.delete_forum_msg(user, date):
            this.load_messages_admin(this.akt_room_id)
            return
        else:
            print("ERROR")

    def update_msg(this, user:str, date:cx_Oracle.Date, frame: tk.Frame) -> None:
        up_frame = tk.Frame(frame)
        up_frame.rowconfigure(index=0, weight=1)
        up_frame.columnconfigure(index=0, weight=1)
        up_frame.columnconfigure(index=1, weight=1)
        up_frame.grid(row=0, column=5, sticky="NESW")

        update_en = tk.Entry(up_frame)
        update_en.grid(row=0, column=0, sticky="NESW")
        ok_btn = tk.Button(up_frame, text="OK", command=partial(this.update_m, up_frame, update_en, user, date))
        ok_btn.grid(row=0, column=1, sticky="NESW")

    def update_m(this, msg_frame: tk.Frame, msg_en: tk.Entry, msg_user:str, msg_date:cx_Oracle.Date):
        this.socialDAO.update_msg(msg_user, msg_date, msg_en.get())
        this.load_messages_admin(this.akt_room_id)
        msg_frame.destroy()


