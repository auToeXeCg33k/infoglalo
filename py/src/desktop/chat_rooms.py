import tkinter as tk
from typing import Union


from .window import Window

class ChatRoom(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        #TITLE ROW
        this.rowconfigure(index=0, weight=1)
        #TITLE ROW 2
        this.rowconfigure(index=1, weight=1)
        #CANVAS
        this.rowconfigure(index=2, weight=1)
        #FOR USERS
        this.columnconfigure(index=0, weight=1)
        #FOR MESSAGES
        this.columnconfigure(index=1, weight=3)


        this.scroll_canvas: Union[None, tk.Canvas] = None
        this.scroll_bar: Union[None, tk.Scrollbar] = None
        this.scrollable_frame: Union[None, tk.Frame] = None

        this.reset()


    #TODO: Rename labels
    def reset(this) -> None:
        #TITLE
        tk.Label(this, text="Közösségi szobák", font=(None, 25)).grid(row=0, column=0, columnspan=2, sticky="NESW")

        #CANVAS FOR CONTENT
        this.scroll_canvas = tk.Canvas(this)
        this.scroll_canvas.grid(row=2, column=0, columnspan=2, sticky="NESW")

        this.scroll_bar = tk.Scrollbar(this, orient="vertical", command=this.scroll_canvas.yview)
        this.scroll_canvas.bind_all("<MouseWheel>", this._on_mousewheel)
        this.scroll_canvas.rowconfigure(index=0, weight=1)
        this.scroll_canvas.columnconfigure(index=0, weight=1)
        this.scroll_bar.grid(row=2, column=1, sticky="NES")

        #FRAME IN THE CANVAS (MAIN FRAME)
        this.scrollable_frame = tk.Frame(this.scroll_canvas)
        this.scrollable_frame.grid(row=0, column=0,sticky="NESW")
        this.scrollable_frame.rowconfigure(index=0, weight=1)
        this.scrollable_frame.columnconfigure(index=0, weight=1)
        this.scrollable_frame.columnconfigure(index=1, weight=3)



        #FRAME FOR ROOM NAME
        room_frame = tk.LabelFrame(this.scrollable_frame, text="Szobak", font=(None, 15))
        room_frame.grid(row=0, column=0,sticky="NESW")

        for i in range(10):
            room_frame.rowconfigure(index=i, weight=1)
            name = "Szoba " + str(i)
            tk.Button(room_frame, command=this.to_room(id), text=name).grid(row=i, column=0, sticky="NESW")

        #FRAME FOR MAIN MESSAGES width=75, height=100
        main_message_frame = tk.LabelFrame(this.scrollable_frame, text="Uzenetek",font=(None, 15))
        main_message_frame.grid(row=0, column=1,sticky="NESW")
        main_message_frame.rowconfigure(index=0, weight=1)
        main_message_frame.rowconfigure(index=1, weight=1)
        main_message_frame.columnconfigure(index=0, weight=1)

        #FRAME FOR MESSAGES
        messages_frame = tk.Frame(main_message_frame)
        messages_frame.grid(row=0, column=0, sticky="NESW")

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

        #CANVAS CONFIGURATIONS
        this.bind("<Configure>",
                        lambda e:
                        this.scroll_canvas.configure(
                            scrollregion=this.scroll_canvas.bbox("all"))
                  )
        this.scroll_canvas.create_window((0, 0), window=this.scrollable_frame, anchor="nw")

        this.scroll_canvas.configure(yscrollcommand=this.scroll_bar.set)


    def _on_mousewheel(this, event):
        this.scroll_canvas.yview_scroll(int(-1*(event.delta/120)), "units")


    def to_room(this, room_id):
        pass


    def send_message(this, content):
        pass