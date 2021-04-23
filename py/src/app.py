import tkinter

from window import Window
from main_menu import MainMenuWindow

from typing import Union
from typing import Type


class App(tkinter.Tk):
    # SAVE CREATED WINDOW IN CACHE
    def create_window(this, name: str, window_type: Type[Window]) -> Union[Window, None]:
        if str in this.windows:
            return None

        window = window_type()
        window.master = this
        this.windows[name] = window
        return window


    # SHOW A CACHED WINDOW
    def show_window(this, name: str) -> bool:
        if name not in this.windows:
            return False

        this.shown = this.windows[name]
        this.shown.reset()
        this.shown.grid(row=0, column=0, sticky="NESW")


    # APP INITIALIZER
    def __init__(this, *args, **kwargs):
        tkinter.Tk.__init__(this, *args, **kwargs)

        # CACHE FOR LOADED WINDOWS
        this.windows: dict[str, Window] = dict()
        # CURRENTLY SHOWN WINDOW
        this.shown: Union[Window, None] = None

        this.title("App")

        this.columnconfigure(index=0, weight=1)
        this.rowconfigure(index=0, weight=1)

        this.create_window("main_menu", MainMenuWindow)
        this.show_window("main_menu")