import tkinter as tk
from abc import abstractmethod
from .window import Window


class ScrollableWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.rowconfigure(index=1, weight=1)
        this.columnconfigure(index=0, weight=1)

        this.canvas = tk.Canvas(this)
        this.scrollbar = tk.Scrollbar(this, orient="vertical", command=this.canvas.yview)
        this.main_frame = tk.Frame(this.canvas)

        this.canvas["bg"] = this["bg"]
        this.main_frame["bg"] = this["bg"]

        this.canvas.grid(row=1, column=0, sticky="NESW")
        this.scrollbar.grid(row=1, column=1, sticky="NES")

        this.canvas.bind("<Configure>", this.resize_frame)
        this.canvas.bind("<MouseWheel>", this._on_mousewheel)
        this.canvas_frame = this.canvas.create_window(0, 0, window=this.main_frame, anchor=tk.NW)
        this.canvas.config(yscrollcommand=this.scrollbar.set)


    def resize_frame(this, event) -> None:
        this.canvas.itemconfig(this.canvas_frame, width=event.width-10, height=event.height-10)
        this.canvas.config(scrollregion=this.canvas.bbox("all"))


    def _on_mousewheel(this, event) -> None:
        this.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    @abstractmethod
    def reset(this) -> None:
        pass