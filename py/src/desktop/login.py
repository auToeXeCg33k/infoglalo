from tkinter import Label
from tkinter.ttk import Entry
from tkinter.ttk import Button
from tkinter import messagebox
import bcrypt
from typing import Union

from .window import Window
from .regist import RegistWindow
from .main_menu import MainMenuWindow
from..core.dao.user_dao import UserDAO


class LoginWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.dao = UserDAO()

        # TEMPORARY WEIGHTS
        this.rowconfigure(index=0, weight=1)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)

        this.uname_entry: Union[None, Entry] = None
        this.pwd_entry: Union[None, Entry] = None

        # TITLE
        Label(this, text="Infoglaló", font=(None, 26)).grid(row=0, column=0, columnspan=2, sticky="NESW")

        # FIELD NAMES
        Label(this, text="Felhasználónév: ").grid(row=1, column=0, sticky="NESW")
        Label(this, text="Jelszó: ").grid(row=2, column=0, sticky="NESW")

        # INPUT FIELDS
        this.uname_entry = Entry(this)
        this.pwd_entry = Entry(this, show="*")

        this.uname_entry.grid(row=1, column=1, sticky="NESW")
        this.pwd_entry.grid(row=2, column=1, sticky="NESW")

        # BUTTONS
        Button(this, text="Regisztráció", command=this.go_to_register).grid(row=3, column=0, sticky="NESW")
        Button(this, text="Bejelentkezés", command=this.login2).grid(row=3, column=1, sticky="NESW")


    def reset(this) -> None:
        this.uname_entry.delete(0, "end")
        this.pwd_entry.delete(0, "end")


    def login(this) -> None:
        # TODO TEMPORARY LOGIN HANDLING
        user = this.dao.get(this.uname_entry.get())
        if user is None:
            messagebox.showerror("Hiba", "Hibás felhasználónév!")
            return

        if user[2] != this.pwd_entry.get():
            messagebox.showerror("Hiba", "Hibás jelszó!")
            return

        this.data["user"] = user
        this.master.raise_window(MainMenuWindow)

    def login2(this) -> None:
        user = this.dao.get(this.uname_entry.get())
        if user is None:
            messagebox.showerror("Hiba", "Hibás felhasználónév!")
            return
        pwd = bytes(user[2], 'utf-8')
        i_pwd=bytes(this.pwd_entry.get(), 'utf-8')

        if not bcrypt.checkpw(i_pwd, pwd):
            messagebox.showerror("Hiba", "Hibás jelszó!")
            return

        this.data["user"] = user
        this.master.raise_window(MainMenuWindow)

    def go_to_register(this) -> None:
        this.master.raise_window(RegistWindow)