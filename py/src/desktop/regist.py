import tkinter
from functools import partial

import bcrypt
from typing import Union
from tkinter import Entry, messagebox, DISABLED
from tkcalendar import Calendar
from ..core.dao.user_dao import UserDAO
from .window import Window


# TODO IMPLEMENT BIRTHDATE
class RegistWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.userDao = UserDAO()

        this.rowconfigure(index=0, weight=1)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=1)
        this.rowconfigure(index=5, weight=1)
        this.rowconfigure(index=6, weight=1)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)

        this.pwd_entry: Union[None, Entry] = None
        this.apwd_entry: Union[None, Entry] = None
        this.uname_entry: Union[None, Entry] = None
        this.email_entry: Union[None, Entry] = None
        this.birthdate_entry: Union[None, Entry] = None

        this.reset()


    def reset(this) -> None:

        tkinter.Label(this, text="Regisztració", font=(None, 25)).grid(row=0, column=0, columnspan=2, sticky="NESW")
        tkinter.Label(this, text="Felhasználónév", font=(None, 15)).grid(row = 1, column=0, sticky="NESW")
        tkinter.Label(this, text="Jelszó", font=(None, 15)).grid(row = 2, column=0, sticky="NESW")
        tkinter.Label(this, text="Jelszó újra", font=(None, 15)).grid(row = 3, column=0, sticky="NESW")
        tkinter.Label(this, text="Email", font=(None, 15)).grid(row=4, column=0, sticky="NESW")
        tkinter.Button(this, command=this.get_date, text="Születési dátum").grid(row=5, column=0, sticky="NESW")


        this.uname_entry = Entry(this)
        this.pwd_entry = Entry(this, show="*")
        this.apwd_entry = Entry(this, show="*")
        this.email_entry = Entry(this)
        this.birthdate_entry = Entry(this)

        this.uname_entry.grid(row=1, column=1, sticky="NESW")
        this.pwd_entry.grid(row=2, column=1, sticky="NESW")
        this.apwd_entry.grid(row=3, column=1, sticky="NESW")
        this.email_entry.grid(row=4, column=1, sticky="NESW")
        this.birthdate_entry.grid(row=5, column=1, sticky="NESW")
        this.birthdate_entry.config(state="disabled")


        tkinter.Button(this, command=this.go_to_login, text="Bejelentkezés").grid(row=6, column=0, sticky="NESW")
        tkinter.Button(this, command=this.regist, text="Regisztráció").grid(row=6, column=1, sticky="NESW")


    def regist(this) -> None:
        if this.pwd_entry.get() != this.apwd_entry.get():
            messagebox.showerror("Hiba", "Nem egyeznek a jelszavak!")
            return

        salt = bcrypt.gensalt()

        b_pwd = bytes(this.pwd_entry.get(), 'utf-8')
        pwd = bcrypt.hashpw(b_pwd, salt)

        this.userDao.insert(this.uname_entry.get(),this.email_entry.get(), pwd.decode("utf-8") , salt.decode("utf-8") , this.birthdate_entry.get())


    def go_to_login(this) -> None:
         this.master.raise_previous_window()

    def get_date(this):
        calendar_frame = tkinter.Toplevel(this)
        cal = Calendar(calendar_frame,
                       font="Arial 14", selectmode='day',
                       cursor="hand1", year=2021, month=5, day=1)
        cal.pack(fill="both", expand=True)
        tkinter.Button(calendar_frame, text="ok", command=partial(this.set_date, cal, this.birthdate_entry, calendar_frame)).pack()

    def set_date(this, calendar:Calendar, enty:Entry, frame:tkinter.Toplevel):
        enty.config(state="normal")
        enty.delete(0,"end")
        enty.insert(0, calendar.selection_get())
        enty.config(state="disabled")
        frame.destroy()