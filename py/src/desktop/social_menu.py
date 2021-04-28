import tkinter as tk

from .chat_rooms import ChatRoom
from .forum import Forum
from .window import Window

class SocialMenu(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.rowconfigure(index=0, weight=2)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)

        this.columnconfigure(index=0, weight=1)

        this.reset()

    def reset(this) -> None:
        tk.Label(this, text="Közösségi menü", font=(None, 25)).grid(row=0, column=0, sticky="NESW")

        tk.Button(this, command=this.go_to_forum, text="Fórum").grid(row=1, column=0, sticky="NESW")
        tk.Button(this, command=this.go_to_rooms, text="Játékos szoba").grid(row=2, column=0, sticky="NESW")
        tk.Button(this, command=this.go_back, text="Vissza").grid(row=3, column=0, sticky="NEWS")



    def go_to_forum(this) -> None:
        this.master.raise_window(Forum)

    def go_to_rooms(this) -> None:
        this.master.raise_window(ChatRoom)

    def go_back(this) -> None:
        this.master.raise_previous_window()

