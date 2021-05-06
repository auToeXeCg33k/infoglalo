import tkinter
from tkinter import ttk

from .chat_rooms import ChatRoom
from .forum import Forum
from .window import Window
from ..core.config import ConfigLoader

class SocialMenu(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.font_family = ConfigLoader.get("font-family")
        this.font_color = ConfigLoader.get("font-color")

        this.rowconfigure(index=0, weight=50)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=20)
        this.rowconfigure(index=4, weight=1)
        this.rowconfigure(index=5, weight=100)

        this.columnconfigure(index=0, weight=1)

        this.reset()

    def reset(this) -> None:
        tkinter.Label(this, fg=this.font_color, text="Közösségi menü", font=(this.font_family, 25), bg=this['bg']).grid(row=0, column=0)

        ttk.Button(this, command=this.go_to_forum, text="Fórum").grid(row=1, column=0)
        ttk.Button(this, command=this.go_to_rooms, text="Játékos szoba").grid(row=2, column=0)
        ttk.Button(this, command=this.go_back, text="Vissza").grid(row=4, column=0)



    def go_to_forum(this) -> None:
        this.master.raise_window(Forum)

    def go_to_rooms(this) -> None:
        this.master.raise_window(ChatRoom)

    def go_back(this) -> None:
        this.master.raise_previous_window()

