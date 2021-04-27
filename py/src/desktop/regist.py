import tkinter
from typing import Union
from tkinter import Entry

from .window import Window
# from .login import LoginWindow


# TODO IMPLEMENT BIRTHDATE
class RegistWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

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

        tkinter.Label(this, text="Regisztració", font=(None, 25)).grid(row=0, column=1, sticky="NESW")
        tkinter.Label(this, text="Felhasználónév", font=(None, 15)).grid(row = 1, column=0, sticky="NESW")
        tkinter.Label(this, text="Jelszó", font=(None, 15)).grid(row = 2, column=0, sticky="NESW")
        tkinter.Label(this, text="Jelszó újra", font=(None, 15)).grid(row = 3, column=0, sticky="NESW")
        tkinter.Label(this, text="Email", font=(None, 15)).grid(row=4, column=0, sticky="NESW")
        tkinter.Label(this, text="Születési dátum", font=(None, 15)).grid(row=5, column=0, sticky="NESW")

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

        # tkinter.Button(this, command=this.go_to_login, text="Bejelentkezés").grid(row=6, column=0, sticky="NESW")
        tkinter.Button(this, command=this.regist, text="Regisztráció").grid(row=6, column=1, sticky="NESW")


    def regist():
        pass

    # def go_to_login(this) -> None:
    #     this.master.show_window(LoginWindow)