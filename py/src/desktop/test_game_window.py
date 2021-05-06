import tkinter
import tkinter.ttk

from .window import Window
from ..core.dao.test_dao import TestDAO


class TestGameWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.dao = TestDAO()
        this.data["test"] = dict()
        this.data["test"]["categories"]: list[str] = list()
        this.data["test"]["difficulties"]: dict[str, int] = {
            "Könnyű": 0,
            "Közepes": 1,
            "Nehéz": 2
        }

        this.current_category = tkinter.StringVar(this)
        this.category_menu = tkinter.ttk.Combobox(this, state="readonly", textvariable=this.current_category)
        this.category_menu.pack()

        this.current_difficulty = tkinter.StringVar(this)
        this.difficulty_menu = tkinter.ttk.Combobox(this, state="readonly", textvariable=this.current_difficulty, values=list(this.data["test"]["difficulties"]))
        this.difficulty_menu.pack()

        tkinter.ttk.Button(master=this, command=this.on_options_selected, text="OK").pack()
        tkinter.ttk.Button(master=this, command=this.go_back, text="Vissza").pack()


    def reset(this) -> None:
        this.data["test"]["categories"].clear()
        this.data["test"]["categories"].extend(this.dao.get_categories())

        this.current_category.set(this.data["test"]["categories"][0])
        this.category_menu["values"] = this.data["test"]["categories"]

        this.current_difficulty.set(list(this.data["test"]["difficulties"])[0])


    def go_back(this) -> None:
        this.master.raise_previous_window()


    def on_options_selected(this) -> None:
        print(this.current_difficulty.get(), this.current_category.get())