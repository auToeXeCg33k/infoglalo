import tkinter

from tkinter.ttk import Button

from .window import Window
from ..core.dao.duel_dao import DuelDAO
from ..core.config import ConfigLoader
from .duel_game_window import DuelGameWindow


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
        highlight_color = ConfigLoader.get("accent-color")

        tkinter.Label(this, font=(font_family, 26), fg=font_color, bg=this["bg"], text="Párbaj").grid(row=0, column=0, columnspan=6, sticky="NEWS")
        tkinter.Label(this, font=(font_family, 18), fg=font_color, bg=this["bg"], text="Kihívottjaid").grid(row=1, column=0, columnspan=2)
        tkinter.Label(this, font=(font_family, 18), fg=font_color, bg=this["bg"], text="Elérhetőek").grid(row=1, column=2, columnspan=2)
        tkinter.Label(this, font=(font_family, 18), fg=font_color, bg=this["bg"], text="Kihívóid").grid(row=1, column=4, columnspan=2)

        this.sent_requests = tkinter.Listbox(this, font=font_family, fg=font_color, bg=this["bg"], bd=0, selectbackground=highlight_color, highlightthickness=0, relief=tkinter.FLAT, selectmode=tkinter.SINGLE)
        this.player_list = tkinter.Listbox(this, font=font_family, fg=font_color, bg=this["bg"], bd=0, selectbackground=highlight_color, highlightthickness=0, relief=tkinter.FLAT, selectmode=tkinter.SINGLE)
        this.incoming_requests = tkinter.Listbox(this, font=font_family, fg=font_color, bg=this["bg"], bd=0, selectbackground=highlight_color, highlightthickness=0, relief=tkinter.FLAT, selectmode=tkinter.SINGLE)

        this.sent_requests.grid(row=2, column=0, columnspan=2, sticky="NESW")
        this.player_list.grid(row=2, column=2, columnspan=2, sticky="NESW")
        this.incoming_requests.grid(row=2, column=4, columnspan=2, sticky="NESW")

        this.sent_requests.config(justify=tkinter.CENTER, activestyle="none")
        this.player_list.config(justify=tkinter.CENTER, activestyle="none")
        this.incoming_requests.config(justify=tkinter.CENTER, activestyle="none")

        # TODO this clears selection before button could query, need another solution
        #this.sent_requests.bind('<FocusOut>', this.deselect_callback)
        #this.player_list.bind('<FocusOut>', this.deselect_callback)
        #this.incoming_requests.bind('<FocusOut>', this.deselect_callback)

        #this.sent_requests.bind('<FocusIn>', this.selection_callback)
        #this.player_list.bind('<FocusIn>', this.selection_callback)
        #this.incoming_requests.bind('<FocusIn>', this.selection_callback)

        revoke_button = Button(this, text="Visszavon", command=this.revoke)
        revoke_button.grid(row=3, column=0, columnspan=2)

        challenge_button = Button(this, text="Kihív", command=this.challenge)
        challenge_button.grid(row=3, column=2, columnspan=2)

        decline_button = Button(this, text="Elutasít", command=this.decline)
        decline_button.grid(row=3, column=4, sticky="E")

        accept_button = Button(this, text="Elfogad", command=this.accept)
        accept_button.grid(row=3, column=5, sticky="W")

        this.sent_requests.buttons = [revoke_button]
        this.player_list.buttons = [challenge_button]
        this.incoming_requests.buttons = [decline_button, accept_button]

        Button(this, text="Vissza", command=this.go_back).grid(row=5, column=0, columnspan=6)


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
        this.dao.delete_duel(this.data["user"][0], this.sent_requests.get(this.sent_requests.curselection())[0], 1)
        this.reset()

    def challenge(this) -> None:
        # TODO start the duel
        this.dao.create_new_duel(this.data["user"][0], this.player_list.get(this.player_list.curselection())[0])
        this.data["duel"] = this.dao.get_unfinished_duel(this.data["user"][0], this.player_list.get(this.player_list.curselection())[0], 1)
        this.data["duel"]["challenger"] = this.data["user"][0]
        this.data["duel"]["challenged"] = this.player_list.get(this.player_list.curselection())[0]

        this.master.raise_window(DuelGameWindow)

    def decline(this) -> None:
        this.dao.delete_duel(this.incoming_requests.get(this.incoming_requests.curselection())[0], this.data["user"][0], 1)
        this.reset()

    def accept(this) -> None:
        this.dao.accept_duel(this.incoming_requests.get(this.incoming_requests.curselection())[0], this.data["user"][0])
        this.data["duel"] = this.dao.get_unfinished_duel(this.incoming_requests.get(this.incoming_requests.curselection())[0], this.data["user"][0], 0)
        this.data["duel"]["challenger"] = this.incoming_requests.get(this.incoming_requests.curselection())[0]
        this.data["duel"]["challenged"] = this.data["user"][0]

        this.master.raise_window(DuelGameWindow)

    def go_back(this) -> None:
        this.master.raise_previous_window()