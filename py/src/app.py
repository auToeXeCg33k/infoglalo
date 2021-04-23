import tkinter

from window import Window
from main_menu import MainMenuWindow

from typing import Union
from typing import Type


class App(tkinter.Tk):
    # SAVE CREATED WINDOW IN CACHE
    def create_window(this, window_type: Type[Window]) -> Union[Window, None]:
        if str in this.windows:
            return None

        window = window_type()
        window.master = this
        this.windows[window_type] = window
        return window


    # SHOW A CACHED WINDOW
    def show_window(this, window_type: Type[Window]) -> bool:
        if window_type not in this.windows:
            return False

        this.shown = this.windows[window_type]
        this.shown.reset()
        this.shown.grid(row=0, column=0, sticky="NESW")


    # APP INITIALIZER
    def __init__(this, *args, **kwargs):
        tkinter.Tk.__init__(this, *args, **kwargs)

        # CACHE FOR LOADED WINDOWS
        this.windows: dict[Type[Window], Window] = dict()
        # CURRENTLY SHOWN WINDOW
        this.shown: Union[Window, None] = None

        this.title("App")

        this.columnconfigure(index=0, weight=1)
        this.rowconfigure(index=0, weight=1)

        this.create_window(MainMenuWindow)
        this.show_window(MainMenuWindow)