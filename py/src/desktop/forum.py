import tkinter
from functools import partial

import cx_Oracle

from .scrollable_window import ScrollableWindow
from core.dao.social_dao import SocialDAO
import tkinter as tk


class Forum(ScrollableWindow):

    def __init__(this, data):
        ScrollableWindow.__init__(this, data)
        # DAO
        this.socialDAO = SocialDAO()

        # FRAME IN THE CANVAS (MAIN FRAME)
        this.main_frame.rowconfigure(index=0, weight=1)
        this.main_frame.rowconfigure(index=1, weight=1)
        this.main_frame.rowconfigure(index=2, weight=1)
        this.main_frame.columnconfigure(index=0, weight=1)

        #tk.Label(this, text="Fórum", font=(None, 25), bg="gray5",fg="snow").pack(expand=0)

        # FRAME FOR MESSAGES
        this.messages_frame = tk.Frame(this.main_frame, bg="blue")
        this.messages_frame.grid(row=0, column=0, sticky="NESW")

        # ADD THE MESSAGES
        if this.data["user"][4]:
            this.load_messages_admin()
        else:
            this.load_messages()

        # MESSAGE WRITER FRAME
        writer_frame = tk.Frame(this)
        writer_frame.rowconfigure(index=0, weight=1)
        writer_frame.columnconfigure(index=0, weight=3)
        writer_frame.columnconfigure(index=1, weight=1)
        writer_frame.columnconfigure(index=2, weight=2)

        msg_entry = tk.Entry(writer_frame)
        msg_entry.grid(row=0, column=0, sticky="NESW", padx=10)

        send_button = tk.Button(writer_frame, text="Send", command=partial(this.send_message, msg_entry, data["user"][0]))
        send_button.grid(row=0, column=1, sticky="NESW", padx=10)

        back_button = tk.Button(writer_frame, text='Vissza', command=this.go_back)
        back_button.grid(row=0, column=2, sticky="W", padx=10)

        writer_frame.pack(side = tkinter.BOTTOM, pady=10)

        #STYLE
        this.messages_frame["bg"] = this["bg"]
        writer_frame["bg"] = this["bg"]

    def reset(this) -> None:
        if this.data["user"][4]:
            this.load_messages_admin()
        else:
            this.load_messages()

    def load_messages(this):
        this.clean_messages()
        room_messages = this.socialDAO.get_forum_messages()

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

    def load_messages_admin(this):
        this.clean_messages()
        room_messages = this.socialDAO.get_forum_messages()
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
            this.load_messages_admin()
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
        this.load_messages_admin()
        msg_frame.destroy()

    def clean_messages(this) -> None:
        for child in this.messages_frame.winfo_children():
            child.destroy()


    def send_message(this, content, user):
        this.socialDAO.send_message(user, 0, content.get())
        content.delete(0, "end")
        this.reset()

    def go_back(this):
        this.master.raise_previous_window()
