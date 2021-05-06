import tkinter

from .window import Window
from ..core.config import ConfigLoader


class DuelGameWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.font_color = ConfigLoader.get("font-color")
        this.font_family = ConfigLoader.get("font-family")

        tkinter.Label(master=this, fg=this.font_color, bg=this["bg"], text="Párbaj").pack(side=tkinter.TOP, fill=tkinter.X)

        print(this.data["duel"])


    def reset(this) -> None:
        pass