import tkinter
from tkinter import ttk

from .window import Window
from ..core.config import ConfigLoader
from ..core.dao.stat_dao import StatDAO
from ..core.dao.toplist_dao import TopListDAO

class StatWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.font_family = ConfigLoader.get("font-family")
        this.font_color = ConfigLoader.get("font-color")

        this.dao = TopListDAO()
        points = this.dao.aggregate()

        this.dao = StatDAO()
        users = this.dao.get_age_stat()



        this.rowconfigure(index=0, weight=30)
        this.rowconfigure(index=1, weight=20)
        this.rowconfigure(index=2, weight=50)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=20)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)

        tkinter.Label(this, fg=this.font_color, text="Statisztikák", bg=this['bg'],
                      font=(this.font_family, 25)).grid(row=0, column=0, columnspan=2)

        tkinter.Label(this, fg=this.font_color, text="Összesített korosztályos statisztika", bg=this['bg'],
                      font=(this.font_family, 18)).grid(row=1, column=0)

        tkinter.Label(this, fg=this.font_color, text=this.data["user"][0] + " témakör szerinti statisztikája", bg=this['bg'],
                      font=(this.font_family, 18)).grid(row=1, column=1)


        ttk.Button(this, text="Vissza", command=this.go_back).grid(row=3, column=0)


    def reset(this) -> None:
        pass

    def go_back(this) -> None:
        this.master.raise_previous_window()