import tkinter

from tkinter.ttk import Button

from .window import Window
from ..core.dao.duel_dao import DuelDAO
from ..core.config import ConfigLoader


class DuelMenuWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.dao = DuelDAO()

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

        font_family = ConfigLoader.get("font-family")
        font_color = ConfigLoader.get("font-color")
        highlight_color = "dark violet"

        tkinter.Label(this, font=(font_family, 26), fg=font_color, bg=this["bg"], text="Párbaj").grid(row=0, column=0, columnspan=6, sticky="NEWS")
        tkinter.Label(this, font=(font_family, 18), fg=font_color, bg=this["bg"], text="Kihívottjaid").grid(row=1, column=0, columnspan=2)
        tkinter.Label(this, font=(font_family, 18), fg=font_color, bg=this["bg"], text="Elérhetőek").grid(row=1, column=2, columnspan=2)
        tkinter.Label(this, font=(font_family, 18), fg=font_color, bg=this["bg"], text="Kihívóid").grid(row=1, column=4, columnspan=2)

        this.sent_requests = tkinter.Listbox(this, font=font_family, fg=font_color, bg=this["bg"], bd=0, selectbackground=highlight_color, highlightthickness=0, relief=tkinter.FLAT)
        this.player_list = tkinter.Listbox(this, font=font_family, fg=font_color, bg=this["bg"], bd=0, selectbackground=highlight_color, highlightthickness=0, relief=tkinter.FLAT)
        this.incoming_requests = tkinter.Listbox(this, font=font_family, fg=font_color, bg=this["bg"], bd=0, selectbackground=highlight_color, highlightthickness=0, relief=tkinter.FLAT)

        this.sent_requests.grid(row=2, column=0, columnspan=2, sticky="NESW")
        this.player_list.grid(row=2, column=2, columnspan=2, sticky="NESW")
        this.incoming_requests.grid(row=2, column=4, columnspan=2, sticky="NESW")

        this.sent_requests.config(justify=tkinter.CENTER, activestyle="none")
        this.player_list.config(justify=tkinter.CENTER, activestyle="none")
        this.incoming_requests.config(justify=tkinter.CENTER, activestyle="none")

        this.sent_requests.bind("<<ListboxSelect>>", this.selection_callback)
        this.player_list.bind("<<ListboxSelect>>", this.selection_callback)
        this.incoming_requests.bind("<<ListboxSelect>>", this.selection_callback)

        this.sent_requests.bind('<FocusOut>', lambda e: this.sent_requests.selection_clear(0, tkinter.END))
        this.player_list.bind('<FocusOut>', lambda e: this.player_list.selection_clear(0, tkinter.END))
        this.incoming_requests.bind('<FocusOut>', lambda e: this.incoming_requests.selection_clear(0, tkinter.END))

        revoke_button = Button(this, text="Visszavon", command=this.revoke, state=tkinter.DISABLED)
        revoke_button.grid(row=3, column=0, columnspan=2)

        challenge_button = Button(this, text="Kihív", command=this.challenge, state=tkinter.DISABLED)
        challenge_button.grid(row=3, column=2, sticky="E")

        decline_button = Button(this, text="Elutasít", command=this.decline, state=tkinter.DISABLED)
        decline_button.grid(row=3, column=3, sticky="W")

        accept_button = Button(this, text="Elfogad", command=this.accept, state=tkinter.DISABLED)
        accept_button.grid(row=3, column=4, columnspan=2)

        this.sent_requests.buttons = [revoke_button]
        this.player_list.buttons = [challenge_button]
        this.incoming_requests.buttons = [decline_button, accept_button]

        Button(this, text="Vissza", command=this.go_back).grid(row=5, column=0, columnspan=6)

        this.reset()


    def reset(this) -> None:
        this.sent_requests.delete(0, this.sent_requests.size() - 1)
        this.player_list.delete(0, this.player_list.size() - 1)
        this.incoming_requests.delete(0, this.incoming_requests.size() - 1)

        this.show_sent_requests()
        this.show_player_list()
        this.show_incoming_requests()


    def deselect_callback(this, event) -> None:
        for button in event.widget.buttons:
            button["state"] = tkinter.DISABLED
        event.widget.selection_clear(0, tkinter.END)


    def selection_callback(this, event) -> None:
        for button in event.widget.buttons:
            button["state"] = tkinter.ACTIVE


    def show_sent_requests(this):
        data = this.dao.get_requested(this.data["user"][0])
        for index, name in enumerate(data):
            this.sent_requests.insert(index, name)

    def show_player_list(this):
        data = this.dao.get_availables(this.data["user"][0])
        for index, name in enumerate(data):
            this.player_list.insert(index, name)

    def show_incoming_requests(this):
        data = this.dao.get_incoming(this.data["user"][0])
        for index, name in enumerate(data):
            this.incoming_requests.insert(index, name)


    def revoke(this) -> None:
        pass

    def challenge(this) -> None:
        pass

    def decline(this) -> None:
        pass

    def accept(this) -> None:
        pass

    def go_back(this) -> None:
        this.master.raise_previous_window()