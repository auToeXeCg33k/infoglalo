import tkinter
from typing import Union
from tkinter import Entry
from .window import Window


class RegistWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.rowconfigure(index=0, weight=1)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=1)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)

        this.pwd_entry: Union[None, Entry] = None
        this.apwd_entry: Union[None, Entry] = None
        this.uname_entry: Union[None, Entry] = None

        this.reset()


    def reset(this) -> None:

        tkinter.Label(this, text="Regisztració", font=(None, 25)).grid(row=0, column=1, sticky="NESW")
        tkinter.Label(this, text="Felhasználónév", font=(None, 15)).grid(row = 1, column=0, sticky="NESW")
        tkinter.Label(this, text="Jelszó", font=(None, 15)).grid(row = 2, column=0, sticky="NESW")
        tkinter.Label(this, text="Jelszó újra", font=(None, 15)).grid(row = 2, column=0, sticky="NESW")

        this.uname_entry = Entry(this)
        this.pwd_entry = Entry(this)
        this.apwd_entry = Entry(this)

        this.uname_entry.grid(row=1, column=1, sticky="NESW")
        this.pwd_entry.grid(row=2, column=1, sticky="NESW")
        this.apwd_entry.grid(row=3, column=1, sticky="NESW")

        tkinter.Button(this, command=this.regist, text="Regisztráció").grid(row=4, column=0, sticky="NESW")


    def regist():
        pass