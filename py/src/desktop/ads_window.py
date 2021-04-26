import tkinter
from .scrollable_window import ScrollableWindow

class AdsWindow(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)
        this.reset()
        
    def reset(this) -> None:
        for i in range (10):
            this.main_frame.rowconfigure(index=i, weight=1)
            tkinter.Label(this.main_frame, text="Valami", font=(None, 25)).grid(row=i, column=0, sticky="NESW")
