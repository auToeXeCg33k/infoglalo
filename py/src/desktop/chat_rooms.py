import tkinter as tk

from .scrollable_window import ScrollableWindow
from ..core.dao.social_dao import SocialDAO

class ChatRoom(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)

        #DAO
        socialDAO = SocialDAO()

        #TITLE
        tk.Label(this, text="Közösségi szobák", font=(None, 25)).grid(row=0, column=0, sticky="NESW")
        #FRAME IN THE CANVAS (MAIN FRAME)
        this.main_frame.rowconfigure(index=0, weight=1)
        this.main_frame.columnconfigure(index=0, weight=1)
        this.main_frame.columnconfigure(index=1, weight=3)

        #FRAME FOR ROOM NAME
        room_frame = tk.LabelFrame(this.main_frame, text="Szobák", font=(None, 15))
        room_frame.grid(row=0, column=0,sticky="NESW")

        #ADD ROOMS FROM DB
        rooms:list[tuple[int, str]] = socialDAO.get_room()

        for i in range(len(rooms)):
            room_frame.rowconfigure(index=i, weight=1)
            tk.Button(room_frame, command=this.to_room(rooms[i][0]), text=rooms[i][1]).grid(row=i, column=0, sticky="NESW")
        

        #FRAME FOR MAIN MESSAGES
        main_message_frame = tk.LabelFrame(this.main_frame, text="Üzenetek",font=(None, 15))
        main_message_frame.grid(row=0, column=1,sticky="NESW")
        main_message_frame.rowconfigure(index=0, weight=1)
        main_message_frame.rowconfigure(index=1, weight=1)
        main_message_frame.columnconfigure(index=0, weight=1)

        #FRAME FOR MESSAGES
        messages_frame = tk.Frame(main_message_frame)
        messages_frame.grid(row=0, column=0, sticky="NESW")


        #ADD MESSAGES FROM DB
        for i in range(15):
            text = "User" + str(i) + ": Ez egy uzenet."
            tk.Label(messages_frame, text=text, font=(None, 10)).grid(row=i, sticky="W")


        #MESSAGE WRITER FRAME
        writer_frame = tk.Frame(main_message_frame)
        writer_frame.rowconfigure(index=0, weight=1)
        writer_frame.columnconfigure(index=0, weight=3)
        writer_frame.columnconfigure(index=1, weight=1)

        msg_entry = tk.Entry(writer_frame)
        msg_entry.grid(row=0, column=0, sticky="NESW")

        send_button = tk.Button(writer_frame, text="Send", command=this.send_message(msg_entry.get()))
        send_button.grid(row=1, column=0, sticky="NESW")

        writer_frame.grid(row=1, column=0, sticky="NESW")

        this.reset()


    def reset(this) -> None:
        pass



    def to_room(this, room_id):
        pass


    def send_message(this, content):
        pass