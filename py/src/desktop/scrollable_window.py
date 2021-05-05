import tkinter
from abc import abstractmethod
from .window import Window


class ScrollableWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.canvas = tkinter.Canvas(master=this, bg=this["bg"], bd=0, highlightthickness=0)
        this.canvas.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)

        this.main_frame = tkinter.Frame(this.canvas, bg=this["bg"])
        this.main_frame.pack(fill=tkinter.BOTH, expand=tkinter.TRUE)

        scrollbar = tkinter.Scrollbar(this.canvas, command=this.canvas.yview)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        this.canvas_window = this.canvas.create_window(0, 0, window=this.main_frame, anchor=tkinter.NW)
        this.canvas.config(yscrollcommand=scrollbar.set)

        this.main_frame.bind("<Configure>", this.on_frame_configure)
        this.canvas.bind("<Configure>", this.on_canvas_configure)


    def on_frame_configure(this, event) -> None:
        this.canvas.config(scrollregion=this.canvas.bbox("all"))

    def on_canvas_configure(this, event) -> None:
        this.canvas.itemconfig(this.canvas_window, width=event.width)

    def _on_mousewheel(this, event) -> None:
        this.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


    @abstractmethod
    def reset(this) -> None:
        pass