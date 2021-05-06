import tkinter

from tkinter.ttk import Button

from .scrollable_window import ScrollableWindow
from ..core.dao.toplist_dao import TopListDAO
from ..core.config import ConfigLoader

from typing import Union


class ToplistWindow(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)

        this.main_frame.rowconfigure(index=0, weight=50)
        this.main_frame.rowconfigure(index=1, weight=1)
        this.main_frame.rowconfigure(index=2, weight=10)
        this.main_frame.rowconfigure(index=3, weight=1)
        this.main_frame.rowconfigure(index=4, weight=20)
        this.main_frame.rowconfigure(index=5, weight=1)
        this.main_frame.rowconfigure(index=6, weight=100)
        this.main_frame.columnconfigure(index=0, weight=1)
        this.main_frame.columnconfigure(index=1, weight=1)
        this.main_frame.columnconfigure(index=2, weight=1)
        this.main_frame.columnconfigure(index=3, weight=1)

        this.aggregate_data: list[str] = list()
        this.easy_data: list[str] = list()
        this.medium_data: list[str] = list()
        this.hard_data: list[str] = list()

        this.display_box: Union[tkinter.Listbox, None] = None

        this.aggregate_label: Union[tkinter.Button, None] = None
        this.easy_label: Union[tkinter.Button, None] = None
        this.medium_label: Union[tkinter.Button, None] = None
        this.hard_label: Union[tkinter.Button, None] = None

        this.highlight_color = "dark violet"

        this.dao = TopListDAO()
        this.reset()

    def reset(this) -> None:
        for child in this.main_frame.winfo_children():
            child.destroy()

        this.aggregate_data, this.easy_data, this.medium_data, this.hard_data = this.query_info()

        font_family = ConfigLoader.get("font-family")
        font_color = ConfigLoader.get("font-color")

        tkinter.Label(this.main_frame, font=(font_family, 26), fg=font_color, bg=this["bg"], text="Rangsor").grid(row=0, column=0, columnspan=4, sticky="NESW")

        this.aggregate_label = tkinter.Label(this.main_frame, font=(font_family, 20), fg=font_color, bg=this["bg"], text="Összesített")
        this.easy_label = tkinter.Label(this.main_frame, font=(font_family, 20), fg=font_color, bg=this["bg"], text="Könnyű")
        this.medium_label = tkinter.Label(this.main_frame, font=(font_family, 20), fg=font_color, bg=this["bg"], text="Közepes")
        this.hard_label = tkinter.Label(this.main_frame, font=(font_family, 20), fg=font_color, bg=this["bg"], text="Nehéz")

        this.aggregate_label.grid(row=1, column=0)
        this.easy_label.grid(row=1, column=1)
        this.medium_label.grid(row=1, column=2)
        this.hard_label.grid(row=1, column=3)

        this.aggregate_label.bind("<Button-1>", lambda e: this.swap_list(this.aggregate_data, this.aggregate_label))
        this.easy_label.bind("<Button-1>", lambda e: this.swap_list(this.easy_data, this.easy_label))
        this.medium_label.bind("<Button-1>", lambda e: this.swap_list(this.medium_data, this.medium_label))
        this.hard_label.bind("<Button-1>", lambda e: this.swap_list(this.hard_data, this.hard_label))

        this.aggregate_label.config(relief=tkinter.FLAT, activebackground=this.highlight_color)
        this.easy_label.config(relief=tkinter.FLAT, activebackground=this.highlight_color)
        this.medium_label.config(relief=tkinter.FLAT, activebackground=this.highlight_color)
        this.hard_label.config(relief=tkinter.FLAT, activebackground=this.highlight_color)

        this.display_box = tkinter.Listbox(this.main_frame, font=font_family, fg=font_color, bg=this["bg"], bd=0, highlightthickness=0, relief=tkinter.FLAT, selectmode=tkinter.SINGLE, justify=tkinter.CENTER, activestyle=tkinter.NONE, selectbackground=this["bg"])
        this.display_box.grid(row=3, column=0, columnspan=4, sticky="NESW")

        Button(this.main_frame, command=this.go_back, text="Vissza").grid(row=5, column=1, columnspan=2)

        this.swap_list(this.aggregate_data, this.aggregate_label)


    def query_info(this) -> tuple[list[str], list[str], list[str], list[str]]:
        aggregate_data = [str(i + 1) + ". " + str(row["USERNAME"]) + "  " + str(row["POINTS"]) + " pont" for i, row in enumerate(sorted(this.dao.aggregate(), key=lambda l: l['POINTS'], reverse=True))]
        easy_data = [str(i + 1) + ". " + data[0] + "  " + str(data[1]) + " pont" for i, data in enumerate(this.dao.easy())]
        medium_data = [str(i + 1) + ". " + data[0] + "  " + str(data[1]) + " pont" for i, data in enumerate(this.dao.medium())]
        hard_data = [str(i + 1) + ". " + data[0] + "  " + str(data[1]) + " pont" for i, data in enumerate(this.dao.hard())]
        return aggregate_data, easy_data, medium_data, hard_data


    def swap_list(this, new_content: list[str], button: tkinter.Label) -> None:
        if this.display_box.size() != 0:
            this.display_box.delete(0, this.display_box.size() - 1)

        for index, content in enumerate(new_content):
            this.display_box.insert(index, content)

        this.aggregate_label["bg"] = this["bg"]
        this.easy_label["bg"] = this["bg"]
        this.medium_label["bg"] = this["bg"]
        this.hard_label["bg"] = this["bg"]

        button["bg"] = this.highlight_color


    def go_back(this) -> None:
        this.master.raise_previous_window()