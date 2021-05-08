import tkinter
from functools import partial
from tkinter import messagebox

from.window import Window
from core.dao.social_dao import SocialDAO
from core.dao.user_dao import UserDAO
import tkinter as tk

class MakeRoom(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        # DAO
        this.socialDAO = SocialDAO()
        this.userDAO = UserDAO()

        this.rowconfigure(index=0, weight=20)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=50)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)

        tk.Label(this, text="Új szoba létrehozása", font=("Ebrima", 25), bg="gray5",fg="snow").grid(row=0, columnspan=2, sticky="NESW")
        tk.Label(this, text="Szoba neve:", font=("Ebrima", 15), bg="gray5",fg="snow").grid(row=1, column=0, sticky="NESW")
        this.name_e = tk.Entry(this)
        this.name_e.grid(row=1, column=1, sticky="NESW", padx=10, pady=15)


        this.canvas = tk.Canvas(this, height = 200, bg=this["bg"])
        this.canvas.grid(row=2, column=0, columnspan=2, sticky="NESW")
        this.canvas.rowconfigure(index=0, weight=1)
        this.canvas.columnconfigure(index=0, weight=1)
        this.canvas.grid_propagate(False)

        this.scrollbar = tk.Scrollbar(this, command=this.canvas.yview)
        this.scrollbar.grid(row=2, column=2, sticky="NES")

        this.users = tk.Frame(this.canvas, height=200, bg=this["bg"])
        this.users.grid(row=0, column=0, sticky="NESW")
        this.users.rowconfigure(index=0, weight=1)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)


        this.in_usr=tk.Frame(this.users, bg=this["bg"])
        this.in_usr.grid(row=0, column=0, sticky="NESW")
        tk.Label(this.in_usr, text="Hozzáadott játékosok", font=("Ebrima", 15), bg="gray5",fg="snow").pack(fill=tk.X, padx=10, pady=15)

        this.non_in_usr=tk.Frame(this.users, bg=this["bg"])
        this.non_in_usr.grid(row=0, column=1, sticky="NESW")
        tk.Label(this.non_in_usr, text="Elérhető játékosok", font=("Ebrima", 15), bg="gray5",fg="snow").pack(fill=tk.X, padx=10, pady=15)

        this.all_users: list[tuple] = this.userDAO.get_all()
        this.in_users: list[str] = list()

        for user in this.all_users:
            tk.Button(this.non_in_usr, text=user[0], command=partial(this.add_to_room, user[0])).pack(fill=tk.X, padx=5, pady=5)


        tk.Button(this, text="Létrehozás", command=this.make_room).grid(row=3, column=0, sticky="NSW", padx=15, pady=15)


        this.canvas_window = this.canvas.create_window(0, 0, window=this.users, anchor=tkinter.NW)
        this.canvas.config(yscrollcommand=this.scrollbar.set)

        this.users.bind("<Configure>", this.on_frame_configure)
        this.canvas.bind("<Configure>", this.on_canvas_configure)
        this.canvas.bind_all("<MouseWheel>", this.on_mouse_wheel)

    def on_frame_configure(this, event) -> None:
        this.canvas.config(scrollregion=this.canvas.bbox("all"))

    def on_canvas_configure(this, event) -> None:
        this.canvas.itemconfig(this.canvas_window, width=event.width)

    def on_mouse_wheel(this, event) -> None:
        if this.canvas.winfo_height() < this.users.winfo_height():
            this.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def ref_list(this):
        tk.Label(this.in_usr, text="Hozzáadott játékosok", font=("Ebrima", 15), bg="gray5",fg="snow").pack(fill=tk.X, padx=10, pady=15)
        tk.Label(this.non_in_usr, text="Elérhető játékosok", font=("Ebrima", 15), bg="gray5",fg="snow").pack(fill=tk.X, padx=10, pady=15)


    def make_room(this):
        room_id = this.socialDAO.get_room_id()
        if this.socialDAO.make_room(room_id, this.name_e.get()):
            for user in this.in_users:
                this.socialDAO.insert_to_room(user, room_id)
            messagebox.showerror("Info", "Sikeres szoba létrehozás!")
            this.master.raise_previous_window()
            return
        messagebox.showerror("Hiba", "Hibás történt!")



    def add_to_room(this, u_name):
        this.in_users.append(u_name)
        for btn in this.non_in_usr.winfo_children():
            if isinstance(btn, tk.Button):
                if btn['text'] == u_name:
                    btn.destroy()
                    tk.Button(this.in_usr, text=u_name).pack(fill=tk.X, padx=5, pady=5)
                    return


    def reset(this) -> None:
        this.name_e.delete(0,'end')

        for user in this.non_in_usr.winfo_children():
            if isinstance(user, tk.Button):
                user.destroy()

        for user in this.in_usr.winfo_children():
            if isinstance(user, tk.Button):
                user.destroy()

        this.all_users = this.userDAO.get_all()
        this.in_users.clear()

        for user in this.all_users:
            tk.Button(this.non_in_usr, text=user[0], command=partial(this.add_to_room, user[0])).pack(fill=tk.X, padx=5, pady=5)



