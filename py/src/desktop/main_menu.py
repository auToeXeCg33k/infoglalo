import tkinter

from tkinter.ttk import Button

from .social_menu import SocialMenu
from .window import Window
from .ads_window import AdsWindow
from .toplist import ToplistWindow
from .play_menu import PlayMenuWindow
from .stat_window import StatWindow
from ..core.config import ConfigLoader

class MainMenuWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.rowconfigure(index=0, weight=50)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=1)
        this.rowconfigure(index=5, weight=1)
        this.rowconfigure(index=6, weight=20)
        this.rowconfigure(index=7, weight=1)
        this.rowconfigure(index=8, weight=100)
        this.columnconfigure(index=0, weight=1)

        this.reset()

    def reset(this) -> None:
        font_family = ConfigLoader.get("font-family")
        font_color = ConfigLoader.get("font-color")

        #MENU TITLE
        tkinter.Label(this, text="Üdv, " + this.data["user"][0] + "!", fg=font_color, bg=this["bg"], font=(font_family, 26)).grid(row=0, column=0)

        #MENU BUTTONS
        Button(this, command=this.go_to_play, text="Játék").grid(row=1, column=0)
        Button(this, command=this.go_to_ranking, text="Rangsor").grid(row=2, column=0)
        Button(this, command=this.go_to_social, text="Közösségi").grid(row=3, column=0)
        Button(this, command=this.go_to_ad, text="Hirdetések").grid(row=4, column=0)
        Button(this, command=this.go_to_stat, text="Statisztika").grid(row=5, column=0)
        Button(this, command=this.logout, text="Kijelentkezés").grid(row=7, column=0)

    def go_to_play(this) -> None:
        this.master.raise_window(PlayMenuWindow)

    def go_to_ranking(this) -> None:
        this.master.raise_window(ToplistWindow)

    def go_to_social(this) -> None:
        this.master.raise_window(SocialMenu)

    def go_to_ad(this) -> None:
        this.master.raise_window(AdsWindow)

    def go_to_stat(this) -> None:
        this.master.raise_window(StatWindow)

    def logout(this):
        del this.data["user"]
        this.master.raise_previous_window()