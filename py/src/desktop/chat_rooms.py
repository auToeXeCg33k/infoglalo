import tkinter as tk
from functools import partial

from .scrollable_window import ScrollableWindow
from ..core.dao.social_dao import SocialDAO

class ChatRoom(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)

        #DAO
        this.socialDAO = SocialDAO()

        #ID FOR THE ACTUAL ROOM
        this.akt_room_id = 1


        #TITLE
        tk.Label(this, text="Közösségi szobák", font=(None, 25)).grid(row=0, column=0, sticky="NESW")
        #FRAME IN THE CANVAS (MAIN FRAME)
        this.main_frame.rowconfigure(index=0, weight=1)
        this.main_frame.columnconfigure(index=0, weight=1)
        this.main_frame.columnconfigure(index=1, weight=3)

        #FRAME FOR ROOM NAME
        this.room_frame = tk.LabelFrame(this.main_frame, text="Szobák", font=(None, 15))
        this.room_frame.grid(row=0, column=0,sticky="NESW")



        #FRAME FOR MAIN MESSAGES
        main_message_frame = tk.LabelFrame(this.main_frame, text="Üzenetek",font=(None, 15))
        main_message_frame.grid(row=0, column=1,sticky="NESW")
        main_message_frame.rowconfigure(index=0, weight=1)
        main_message_frame.rowconfigure(index=1, weight=1)
        main_message_frame.columnconfigure(index=0, weight=1)

        #FRAME FOR MESSAGES
        messages_frame = tk.Frame(main_message_frame)
        messages_frame.grid(row=0, column=0, sticky="NESW")


        #ADD ROOMS AND MESSAGES FROM DB
        rooms:list[tuple[int, str]] = this.socialDAO.get_room()

        for i in range(len(rooms)):
            this.room_frame.rowconfigure(index=i, weight=1)
            tk.Button(this.room_frame, command=partial(this.to_room, rooms[i][0], messages_frame), text=rooms[i][1]).grid(row=i, column=0, sticky="NEW")


        #MESSAGE WRITER FRAME
        writer_frame = tk.Frame(main_message_frame)
        writer_frame.rowconfigure(index=0, weight=1)
        writer_frame.columnconfigure(index=0, weight=3)
        writer_frame.columnconfigure(index=1, weight=1)

        msg_entry = tk.Entry(writer_frame)
        msg_entry.grid(row=0, column=0, sticky="NESW")

        send_button = tk.Button(writer_frame, text="Send", command=partial(this.send_message,this.akt_room_id, msg_entry))
        send_button.grid(row=1, column=0, sticky="NESW")

        writer_frame.grid(row=1, column=0, sticky="NESW")

        this.reset()


    def reset(this) -> None:
        pass



    def to_room(this, room_id:int, frame:tk.Frame) -> None:
        room_messages = this.socialDAO.get_messages(room_id)
        this.akt_room_id = room_id
        for i in range(len(room_messages)):
            text = "User" + room_messages[i][0] + ":" + room_messages[i][3]
            tk.Label(frame, text=text, font=(None, 10)).grid(row=i, sticky="W")



    def send_message(this, room_id, content:tk.Entry):
        print(this.socialDAO.send_message("Atesz", room_id, content.get()))
        content.delete(0,"end")
        this.reset()