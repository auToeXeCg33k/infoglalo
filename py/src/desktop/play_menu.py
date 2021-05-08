import tkinter

from tkinter.ttk import Button

from .window import Window
from .iq_game_window import IQWindow
from .duel_menu import DuelMenuWindow
from .test_game_window import TestGameWindow
from core.config import ConfigLoader


class PlayMenuWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.rowconfigure(index=0, weight=50)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=1)
        this.rowconfigure(index=5, weight=20)
        this.rowconfigure(index=6, weight=1)
        this.rowconfigure(index=7, weight=100)
        this.columnconfigure(index=0, weight=1)

        this.reset()

    def reset(this) -> None:
        font_family = ConfigLoader.get("font-family")
        font_color = ConfigLoader.get("font-color")

        #MENU TITLE
        tkinter.Label(this, text="Válassz játékmódot!", fg=font_color, bg=this["bg"], font=(font_family, 26)).grid(row=0, column=0, sticky="NESW")

        #MENU BUTTONS
        Button(this, command=this.go_to_iq, text="IQ teszt").grid(row=1, column=0)
        Button(this, command=this.go_to_comp, text="Verseny").grid(row=2, column=0)
        Button(this, command=this.go_to_duel, text="Párbaj").grid(row=3, column=0)
        Button(this, command=this.go_to_test, text="Tematikus teszt").grid(row=4, column=0)
        Button(this, command=this.go_back, text="Vissza").grid(row=6, column=0)

    def go_to_iq(this) -> None:
        this.master.raise_window(IQWindow)

    def go_to_comp(this) -> None:
        pass

    def go_to_duel(this) -> None:
        this.master.raise_window(DuelMenuWindow)

    def go_to_test(this) -> None:
        this.master.raise_window(TestGameWindow)

    def go_back(this) -> None:
        this.master.raise_previous_window()
