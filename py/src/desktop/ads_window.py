import tkinter as tk
from tkinter import ttk

from .new_ads_window import NewAdsWindow
from .scrollable_window import ScrollableWindow
from ..core.dao.ad_dao import AdDAO
from ..core.config import ConfigLoader


class AdsWindow(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)

        this.font_family = ConfigLoader.get("font-family")
        this.font_color = ConfigLoader.get("font-color")

        this.main_frame.columnconfigure(index=0, weight=1)
        this.main_frame.columnconfigure(index=1, weight=1)

        tk.Label(this, fg=this.font_color, text="Hirdetések", bg=this['bg'], font=(this.font_family, 25)).grid(row=0, column=0, sticky="NESW")

        this.reset()

    def reset(this) -> None:
        for child in this.main_frame.winfo_children():
            child.destroy()

        dao = AdDAO()
        data = dao.find_all()
        i = 0
        for i in range (len(data)):
            this.main_frame.rowconfigure(index=i, weight=1)
            img_button = ttk.Button(this.main_frame, image=data[i][2], command=lambda index=i: this.get_info(data, index))
            img_button.image = data[i][2]
            img_button.grid(row=i, column=0, columnspan=2)
        this.main_frame.rowconfigure(index=i+1, weight=1)
        tk.Button(this.main_frame, text="Vissza", command=this.go_back).grid(row=i+1, column=0, sticky="NESW")

        if this.data["user"][4]: # ha admin
            ttk.Button(this.main_frame, text="Hirdetés felvitele", command=this.go_admin).grid(row=i+1, column=1, sticky="NESW")


    def get_info(this, data, i) -> None:
        info_frame = tk.Toplevel()
        info_frame.columnconfigure(index=0, weight=1)
        info_frame.rowconfigure(index=0, weight=1)
        info_frame.rowconfigure(index=1, weight=0)
        tk.Label(info_frame, fg=this.font_color, text=data[i][0], bg=this['bg'], font=(this.font_family, 25)).grid(row=0, column=0, sticky="NESW")
        tk.Label(info_frame, fg=this.font_color, text=data[i][1], bg=this['bg'], font=(this.font_family, 15)).grid(row=1, column=0, sticky="NESW")

    def go_back(this) -> None:
        this.master.raise_previous_window()

    def go_admin(this) -> None:
        this.master.raise_window(NewAdsWindow)


