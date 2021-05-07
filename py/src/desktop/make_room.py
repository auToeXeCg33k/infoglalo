import tkinter

from.window import Window
from ..core.dao.social_dao import SocialDAO
from ..core.dao.user_dao import UserDAO
import tkinter as tk

class MakeRoom(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        # DAO
        this.socialDAO = SocialDAO()
        this.userDAO = UserDAO()

        this.rowconfigure(index=0, weight=50)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=100)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)

        tk.Label(this, text="Új szoba létrehozása", font=("Ebrima", 25), bg="gray5",fg="snow").grid(row=0, columnspan=2, sticky="NESW")
        tk.Label(this, text="Szoba neve:", font=("Ebrima", 15), bg="gray5",fg="snow").grid(row=1, column=0, sticky="NESW")
        this.name_e = tk.Entry(this).grid(row=1, column=1, sticky="NESW")

        this.users = tk.Frame(this)
        this.users.grid(row=2, column=0, columnspan=2, sticky="NESW")
        this.users.rowconfigure(index=0, weight=1)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=0, weight=1)


        this.in_usr=tk.Frame(this.users)
        this.in_usr.grid(row=0, column=0, sticky="NESW")

        this.non_in_usr=tk.Frame(this.users)
        this.non_in_usr.grid(row=0, column=1, sticky="NESW")

        all_users: list[tuple] = this.userDAO.get_all()

        for user in all_users:
            tk.Button(this.non_in_usr, text=user[0]).pack(fill=tk.X, padx=10, pady=10)






    def reset(this) -> None:
        pass