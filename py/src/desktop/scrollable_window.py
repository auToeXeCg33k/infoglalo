from typing import Union
import tkinter as tk
from .window import Window


class ScrollableWindow(Window):

    def __init__(this, data) -> None:
        Window.__init__(this, data)

        #TITLE ROW
        # this.rowconfigure(index=0, weight=1)
        #CANVAS ROW
        this.rowconfigure(index=1, weight=1)

        this.columnconfigure(index=0, weight=1)

        #SCROLLABLE CANVAS
        this.scroll_canvas: Union[None, tk.Canvas] = tk.Canvas(this)
        this.scroll_bar: Union[None, tk.Scrollbar] = tk.Scrollbar(this)
        #MAIN FRAME IN THE CANVAS
        this.main_frame: Union[None, tk.Frame] = tk.Frame(this.scroll_canvas)

        # CANVAS CONF.
        this.scroll_canvas.grid(row=1, column=0, sticky="NESW")
        this.scroll_bar = tk.Scrollbar(this, orient="vertical", command=this.scroll_canvas.yview)
        this.canvas_conf()
        # BIND THE MOUSEWHEEL ACTION
        this.scroll_canvas.bind_all("<MouseWheel>", this._on_mousewheel)
        this.scroll_bar.grid(row=1, column=0, sticky="NES")
        this.scroll_canvas.rowconfigure(index=0, weight=1)
        this.scroll_canvas.columnconfigure(index=0, weight=1)


    def canvas_conf(this) -> None:
        this.bind("<Configure>",
                  lambda e:
                  this.scroll_canvas.configure(
                      scrollregion=this.scroll_canvas.bbox("all"))
                  )

        this.scroll_canvas.create_window((0, 0), window=this.main_frame, anchor="nw")

        this.scroll_canvas.configure(yscrollcommand=this.scroll_bar.set)

    def _on_mousewheel(this, event) -> None:
        this.scroll_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
