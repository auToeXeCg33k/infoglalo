import tkinter

from .window import Window
from .login import LoginWindow

from typing import Type


class App(tkinter.Tk):
    # CACHE AND PUT WINDOW ON THE BACK STACK
    def raise_window(this, window_type: Type[Window]) -> None:
        if window_type not in this.windows:
            window = window_type(this.data)
            window.master = this
            this.windows[window_type] = window

        this.back_stack.append(this.windows[window_type])
        this.back_stack[-1].reset()
        this.back_stack[-1].grid(row=0, column=0, sticky="NESW")


    # GO BACK ONE STEP IN THE BACK STACK
    def raise_previous_window(this) -> None:
        this.back_stack[-1].grid_forget()
        this.back_stack.pop()
        this.back_stack[-1].reset()


    # APP INITIALIZER
    def __init__(this, *args, **kwargs):
        tkinter.Tk.__init__(this, *args, **kwargs)

        this.geometry("960x540")
        this.minsize(800, 600)
        this["bg"] = "gray10"

        # CACHE FOR LOADED WINDOWS
        this.windows: dict[Type[Window], Window] = dict()
        # WINDOW BACK STACK
        this.back_stack: list[Window] = list()

        # CENTRAL DATA HOLDER
        this.data: dict[str] = dict()

        this.title("Infoglaló")

        this.columnconfigure(index=0, weight=1)
        this.rowconfigure(index=0, weight=1)

        this.raise_window(LoginWindow)
