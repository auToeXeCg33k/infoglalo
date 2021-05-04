import tkinter

from tkinter.ttk import Button

from .window import Window
from ..core.dao.duel_dao import DuelDAO
from ..core.config import ConfigLoader


class DuelMenuWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.rowconfigure(index=0, weight=50)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=20)
        this.rowconfigure(index=5, weight=1)
        this.rowconfigure(index=6, weight=100)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)
        this.columnconfigure(index=2, weight=1)
        this.columnconfigure(index=3, weight=1)
        this.columnconfigure(index=4, weight=1)
        this.columnconfigure(index=5, weight=1)

        this.dao = DuelDAO()
        this.reset()

    def reset(this) -> None:
        for child in this.winfo_children():
            child.destroy()

        font_family = ConfigLoader.get("font-family")
        font_color = ConfigLoader.get("font-color")
        highlight_color = "dark violet"

        tkinter.Label(this, font=(font_family, 26), fg=font_color, bg=this["bg"], text="Párbaj").grid(row=0, column=0, columnspan=6, sticky="NEWS")
        tkinter.Label(this, font=(font_family, 18), fg=font_color, bg=this["bg"], text="Kihívottjaid").grid(row=1, column=0, columnspan=2)
        tkinter.Label(this, font=(font_family, 18), fg=font_color, bg=this["bg"], text="Elérhetőek").grid(row=1, column=2, columnspan=2)
        tkinter.Label(this, font=(font_family, 18), fg=font_color, bg=this["bg"], text="Kihívóid").grid(row=1, column=4, columnspan=2)

        sent_requests = tkinter.Listbox(this, font=font_family, fg=font_color, bg=this["bg"], bd=0, selectbackground=highlight_color, highlightthickness=0, relief=tkinter.FLAT)
        player_list = tkinter.Listbox(this, font=font_family, fg=font_color, bg=this["bg"], bd=0, selectbackground=highlight_color, highlightthickness=0, relief=tkinter.FLAT)
        incoming_requests = tkinter.Listbox(this, font=font_family, fg=font_color, bg=this["bg"], bd=0, selectbackground=highlight_color, highlightthickness=0, relief=tkinter.FLAT)

        sent_requests.grid(row=2, column=0, columnspan=2, sticky="NESW")
        player_list.grid(row=2, column=2, columnspan=2, sticky="NESW")
        incoming_requests.grid(row=2, column=4, columnspan=2, sticky="NESW")

        sent_requests.config(justify=tkinter.CENTER, activestyle="none")
        player_list.config(justify=tkinter.CENTER, activestyle="none")
        incoming_requests.config(justify=tkinter.CENTER, activestyle="none")

        Button(this, text="Visszavon", command=this.rewoke).grid(row=3, column=0, columnspan=2)
        Button(this, text="Kihív", command=this.challenge).grid(row=3, column=2, sticky="E")
        Button(this, text="Elutasít", command=this.decline).grid(row=3, column=3, sticky="W")
        Button(this, text="Elfogad", command=this.accept).grid(row=3, column=4, columnspan=2)
        Button(this, text="Vissza", command=this.go_back).grid(row=5, column=0, columnspan=6)

        this.show_sent_requests(sent_requests)
        this.show_player_list(player_list)
        this.show_incoming_requests(incoming_requests)

    def show_sent_requests(this, listbox):
        data = this.dao.get_requested(this.data["user"][0])
        for index, name in enumerate(data):
            listbox.insert(index, name)

    def show_player_list(this, listbox):
        data = this.dao.get_availables(this.data["user"][0])
        for index, name in enumerate(data):
            listbox.insert(index, name)

    def show_incoming_requests(this, listbox):
        data = this.dao.get_incoming(this.data["user"][0])
        for index, name in enumerate(data):
            listbox.insert(index, name)

    def rewoke(this) -> None:
        pass

    def challenge(this) -> None:
        pass

    def decline(this) -> None:
        pass

    def accept(this) -> None:
        pass

    def go_back(this) -> None:
        this.master.raise_previous_window()