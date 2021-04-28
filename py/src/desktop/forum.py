from functools import partial

from .scrollable_window import ScrollableWindow
from ..core.dao.social_dao import SocialDAO
import tkinter as tk


class Forum(ScrollableWindow):

    def __init__(this, data):
        ScrollableWindow.__init__(this, data)
        # DAO
        this.socialDAO = SocialDAO()

        # TITLE
        tk.Label(this, text="Fórum", font=(None, 25)).grid(row=0, column=0, sticky="NESW")
        # FRAME IN THE CANVAS (MAIN FRAME)
        this.main_frame.rowconfigure(index=0, weight=1)
        this.main_frame.rowconfigure(index=1, weight=1)
        this.main_frame.columnconfigure(index=0, weight=1)

        # FRAME FOR MAIN MESSAGES
        main_message_frame = tk.LabelFrame(this.main_frame, text="Üzenetek", font=(None, 15))
        main_message_frame.grid(row=0, column=0, sticky="NEW")
        main_message_frame.rowconfigure(index=0, weight=1)
        main_message_frame.rowconfigure(index=1, weight=1)
        main_message_frame.columnconfigure(index=0, weight=1)

        # FRAME FOR MESSAGES
        messages_frame = tk.Frame(main_message_frame)
        messages_frame.grid(row=0, column=0, sticky="NESW")

        # ADD THE MESSAGES
        room_messages = this.socialDAO.get_forum_messages()

        for i in range(len(room_messages)):
            akt_message = tk.Frame(messages_frame)
            akt_message.rowconfigure(index=0, weight=1)
            akt_message.columnconfigure(index=0, weight=1)
            akt_message.columnconfigure(index=1, weight=3)
            akt_message.columnconfigure(index=2, weight=1)
            tk.Label(akt_message, text=room_messages[i][0], font=(None, 10)).grid(row=0, column=0, sticky="W")
            tk.Label(akt_message, text=room_messages[i][3], font=(None, 10)).grid(row=0, column=1, sticky="WE")
            tk.Label(akt_message, text=room_messages[i][2], font=(None, 10)).grid(row=0, column=2, sticky="E")
            akt_message.grid(row=i, sticky="W")



        # MESSAGE WRITER FRAME
        writer_frame = tk.Frame(main_message_frame)
        writer_frame.rowconfigure(index=0, weight=1)
        writer_frame.columnconfigure(index=0, weight=3)
        writer_frame.columnconfigure(index=1, weight=1)

        msg_entry = tk.Entry(writer_frame)
        msg_entry.grid(row=0, column=0, sticky="NESW")

        send_button = tk.Button(writer_frame, text="Send", command=partial(this.send_message, msg_entry))
        send_button.grid(row=1, column=0, sticky="NESW")

        writer_frame.grid(row=1, column=0, sticky="ESW")

        # BACK BUTTON
        back_button = tk.Button(this.main_frame, text='Vissza', command=this.go_back)
        back_button.grid(row=1, column=0, sticky="W")

    def reset(this) -> None:
        pass

    def send_message(this, content):
        pass

    def go_back(this):
        this.master.raise_previous_window()
