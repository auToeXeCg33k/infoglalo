import tkinter

from window import Window
from login import LoginWindow

from typing import Union
from typing import Type


class App(tkinter.Tk):
    # SHOW A CACHED WINDOW
    def show_window(this, window_type: Type[Window]) -> None:
        if window_type not in this.windows:
            window = window_type()
            window.master = this
            this.windows[window_type] = window

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

        this.title("Infoglaló")

        this.columnconfigure(index=0, weight=1)
        this.rowconfigure(index=0, weight=1)

        this.show_window(LoginWindow)