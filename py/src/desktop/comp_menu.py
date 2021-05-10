import tkinter
from functools import partial
from tkinter import messagebox
from datetime import datetime, timedelta
from tkinter.ttk import Button

import cx_Oracle
from tkcalendar import Calendar

from core.dao.comp_dao import CompDAO
from .comp_game_window import CompGameWindow
from .window import Window
from core.config import ConfigLoader


class CompMenuWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.selected = ""

        this.dao = CompDAO()

        this.data["in_game"] = dict()

        this.rowconfigure(index=0, weight=50)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=20)
        this.rowconfigure(index=5, weight=1)
        this.rowconfigure(index=6, weight=1)
        this.rowconfigure(index=7, weight=100)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)
        this.columnconfigure(index=2, weight=1)
        this.columnconfigure(index=3, weight=1)
        this.columnconfigure(index=4, weight=1)
        this.columnconfigure(index=5, weight=1)

        this.font_family = ConfigLoader.get("font-family")
        this.font_color = ConfigLoader.get("font-color")
        this.highlight_color = ConfigLoader.get("accent-color")


        tkinter.Label(this, font=(this.font_family, 26), fg=this.font_color, bg=this["bg"], text="Verseny").grid(row=0, column=0, columnspan=6, sticky="NEWS")
        tkinter.Label(this, font=(this.font_family, 18), fg=this.font_color, bg=this["bg"], text="Versenyek").grid(row=1, column=0, columnspan=2)
        tkinter.Label(this, font=(this.font_family, 18), fg=this.font_color, bg=this["bg"], text="Verseny jelentkezesek").grid(row=1, column=2, columnspan=2)
        tkinter.Label(this, font=(this.font_family, 18), fg=this.font_color, bg=this["bg"], text="Aktiv utkozetek").grid(row=1, column=4, columnspan=2)


        this.all_comp = tkinter.Listbox(this, font=this.font_family, fg=this.font_color, bg=this["bg"], bd=0, selectbackground=this.highlight_color, highlightthickness=0, relief=tkinter.FLAT, selectmode=tkinter.SINGLE)
        this.my_comp = tkinter.Listbox(this, font=this.font_family, fg=this.font_color, bg=this["bg"], bd=0, selectbackground=this.highlight_color, highlightthickness=0, relief=tkinter.FLAT, selectmode=tkinter.SINGLE)
        this.akt_play = tkinter.Listbox(this, font=this.font_family, fg=this.font_color, bg=this["bg"], bd=0, selectbackground=this.highlight_color, highlightthickness=0, relief=tkinter.FLAT, selectmode=tkinter.SINGLE)


        this.all_comp.grid(row=2, column=0, columnspan=2, sticky="NESW")
        this.my_comp.grid(row=2, column=2, columnspan=2, sticky="NESW")
        this.akt_play.grid(row=2, column=4, columnspan=2, sticky="NESW")


        this.all_comp.config(justify=tkinter.CENTER, activestyle="none")
        this.my_comp.config(justify=tkinter.CENTER, activestyle="none")
        this.akt_play.config(justify=tkinter.CENTER, activestyle="none")


        ap_button = Button(this, text="Jelentkezes", command=this.join_comp)
        ap_button.grid(row=3, column=0, columnspan=2)

        start_button = Button(this, text="Verseny inditas", command=this.start_comp)
        start_button.grid(row=3, column=2, columnspan=2)

        start_play = Button(this, text="Utkozet inditas", command=this.start_play)
        start_play.grid(row=3, column=4, columnspan=2)

        this.all_comp.buttons = [ap_button]
        this.my_comp.buttons = [start_button]
        this.akt_play.buttons = [start_play]


        Button(this, text="Vissza", command=this.go_back).grid(row=5, column=0, columnspan=6)
        if this.data["user"][4]:
            Button(this, text="Uj verseny", command=this.make_new).grid(row=6, column=0, columnspan=6)


    def start_comp(this):
        id = this.my_comp.get(this.my_comp.curselection())[0]


        if this.dao.get_free_space(id) > 0 and not this.dao.run_comp(id):
            messagebox.showerror("Hiba", "Keves jatekos nevezett!")
            return
        if this.dao.get_free_space(id) == 0 and this.dao.run_comp(id):
            messagebox.showerror("Hiba", "A verseny mar jut!")
            return
        if this.dao.get_free_space(id) == 0 and this.dao.is_playing(id, this.data["user"][0]):
            messagebox.showinfo("Info", "Van aktiv utkozeted ebben a versenyben!")
            return
        if this.dao.get_free_space(id) == 0 and not this.dao.is_playing(id, this.data["user"][0]):
            this.alloc(id)
            return

    def alloc(this, r_id):
        users = this.dao.get_players(r_id)
        first_date = (datetime.now()).strftime('%Y-%m-%d-%H:%M:%S')
        second_date = (datetime.now()).strftime('%Y-%m-%d-%H:%M:%S')
        print(first_date)
        if this.dao.get_number(r_id) == 4:
            for i in range(4):
                if i < 2:
                    this.dao.join_play(int(r_id), users[i][1], str(first_date))
                else:
                    this.dao.join_play(int(r_id), users[i][1], str(second_date))
        else:
            for i in range(6):
                if i < 3:
                    this.dao.join_play(int(r_id), users[i][1], str(first_date))
                else:
                    this.dao.join_play(int(r_id), users[i][1], str(second_date))

        this.reset()


    def start_play(this):
        index = this.akt_play.curselection()
        row = this.akt_play.get(index)
        name = str(row).split(" ")
        id = this.dao.get_comp_id(name[1][0:-1])[0][0]
        this.data["comp"] = this.dao.get_random_question(id)
        this.master.raise_window(CompGameWindow)
        return


    def go_back(this) -> None:
        this.master.raise_previous_window()

    def reset(this) -> None:
        this.all_comp.delete(0, this.all_comp.size() - 1)
        this.my_comp.delete(0, this.my_comp.size() - 1)
        this.akt_play.delete(0, this.akt_play.size() - 1)

        this.show_all()
        this.show_my()
        this.show_play()

    def make_new(this):
        new_comp = tkinter.Toplevel(this)
        new_comp.rowconfigure(index=0, weight=1)
        new_comp.rowconfigure(index=1, weight=1)
        new_comp.rowconfigure(index=2, weight=1)
        new_comp.rowconfigure(index=3, weight=1)
        new_comp.rowconfigure(index=4, weight=1)
        new_comp.columnconfigure(index=0, weight=1)
        new_comp.columnconfigure(index=1, weight=1)

        tkinter.Label(new_comp, font=(this.font_family, 20), fg=this.font_color, bg=this["bg"], text="Uj verseny").grid(row=0, column=0, columnspan=2, sticky="NESW")
        tkinter.Label(new_comp, font=(this.font_family, 15), fg=this.font_color, bg=this["bg"], text="Verseny neve:").grid(row=1, column=0, sticky="NESW")
        tkinter.Label(new_comp, font=(this.font_family, 15), fg=this.font_color, bg=this["bg"], text="Jatekosszam:").grid(row=3, column=0, sticky="NESW")

        itemsforlistbox=['4','6']

        mylistbox=tkinter.Listbox(new_comp, font=('times',15), height = 2)
        mylistbox.bind('<<ListboxSelect>>',this.CurSelet)
        mylistbox.grid(row=3, column=1, sticky="NESW")
        mylistbox['bg'] = this['bg']

        for items in itemsforlistbox:
            mylistbox.insert(tkinter.END,items)

        n_entry = tkinter.Entry(new_comp)
        n_entry.grid(row=1, column=1, sticky="NESW")

        d_entry = tkinter.Entry(new_comp)
        d_entry.grid(row=2, column=1, sticky="NESW")


        tkinter.Button(new_comp, text="Idopont", command=partial(this.get_date, new_comp, d_entry)).grid(row=2, column=0, sticky="NESW")
        tkinter.Button(new_comp, text="OK", command=partial(this.make_comp, n_entry, new_comp, d_entry)).grid(row=4, column=0, sticky="NESW")

    def CurSelet(this,event):
        widget = event.widget
        selection=widget.curselection()
        picked = widget.get(selection)
        this.selected = picked



    def make_comp(this, comp_name, frame:tkinter.Frame, start):
        this.dao.new_comp(this.dao.get_new_id(), comp_name.get(), start.get(), this.selected)
        frame.destroy()
        this.reset()

    def get_date(this, frame:tkinter.Frame, start:tkinter.Entry):
        calendar_frame = tkinter.Toplevel(frame)
        cal = Calendar(calendar_frame,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2021, month=5, day=1)
        cal.pack(fill="both", expand=True)
        tkinter.Button(calendar_frame, text="ok", command=partial(this.set_date, cal, start, calendar_frame)).pack()

    def set_date(this, calendar:Calendar, enty:tkinter.Entry, frame:tkinter.Toplevel):
        enty.config(state="normal")
        enty.delete(0,"end")
        enty.insert(0, calendar.selection_get())
        enty.config(state="disabled")
        frame.destroy()


    def show_all(this):
        data = this.dao.get_all_comp(this.data["user"][0])
        for index, name in enumerate(data):
            this.all_comp.insert(index, name)

    def show_my(this):
        data = this.dao.get_my_comp(this.data["user"][0])
        for index, name in enumerate(data):
            this.my_comp.insert(index, name)


    def show_play(this):
        data = this.dao.get_play(this.data["user"][0])
        for i in range(len(data)):
            szoveg = "Verseny: " + data[i][0] + ", kezdes: " + str(data[i][1])
            this.akt_play.insert(i, szoveg)


    def join_comp(this):
        if this.dao.get_free_space(this.all_comp.get(this.all_comp.curselection())[0]) <= 0:
            messagebox.showerror("Hiba", "A verseny megtelt!")
            return
        this.dao.join_comp(this.all_comp.get(this.all_comp.curselection())[0], this.data["user"][0])
        this.reset()


    def deselect_callback(this, event) -> None:
        for button in event.widget.buttons:
            button["state"] = tkinter.DISABLED

    def selection_callback(this, event) -> None:
        for button in event.widget.buttons:
            button["state"] = tkinter.ACTIVE
