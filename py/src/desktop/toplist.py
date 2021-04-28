import tkinter

from .scrollable_window import ScrollableWindow

# TODO
class ToplistWindow(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)

        this.main_frame.rowconfigure(index=0, weight=1)
        this.main_frame.columnconfigure(index=0, weight=1)
        tkinter.Button(this.main_frame, command=this.go_back, text="Vissza").grid(row=0, column=0, sticky="NESW")

        this.reset()

    def reset(this) -> None:
        pass


    def go_back(this) -> None:
        this.master.raise_previous_window()