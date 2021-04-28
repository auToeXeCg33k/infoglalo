import tkinter as tk

from .window import Window
from ..core.dao.duel_dao import DuelDAO

class DuelMenuWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.rowconfigure(index=0, weight=1)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)
        this.columnconfigure(index=2, weight=1)
        this.columnconfigure(index=3, weight=1)
        this.columnconfigure(index=4, weight=1)
        this.columnconfigure(index=5, weight=1)
        this.columnconfigure(index=6, weight=1)

        this.dao = DuelDAO()
        this.reset()

    def reset(this) -> None:
        for child in this.winfo_children():
            child.destroy()

        tk.Label(this, text="Párbaj menü").grid(row=0, column=0, sticky="NEWS")

        tk.Button(this, text="Visszavon", command=this.rewoke).grid(row=2, column=1, columnspan=2, sticky="NEWS")
        tk.Button(this, text="Kihív", command=this.challenge).grid(row=2, column=3, columnspan=2, sticky="NEWS")
        tk.Button(this, text="Elutasít", command=this.decline).grid(row=2, column=5, sticky="NEWS")
        tk.Button(this, text="Elfogad", command=this.accept).grid(row=2, column=6, sticky="NEWS")

        sent_requests = tk.Listbox(this)
        player_list = tk.Listbox(this)
        incoming_requests = tk.Listbox(this)

        sent_requests.grid(row=1, column=1, sticky="NS")
        player_list.grid(row=1, column=2, sticky="NS")
        incoming_requests.grid(row=1, column=3, sticky="NS")

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
