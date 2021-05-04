import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import os

from .window import Window
from ..core.config import ConfigLoader
from ..core.dao.ad_dao import AdDAO

class NewAdsWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.rowconfigure(index=0, weight=50)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=1)
        this.rowconfigure(index=5, weight=1)
        this.rowconfigure(index=6, weight=70)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)

        this.font_family = ConfigLoader.get("font-family")
        this.font_color = ConfigLoader.get("font-color")

        tkinter.Label(this, fg=this.font_color, bg=this['bg'], text="Hirdetés felvitele", font=(this.font_family, 25)).grid(row=0, column=0, columnspan=2)
        tkinter.Label(this, fg=this.font_color, bg=this['bg'], text="Cím", font=(this.font_family, 15)).grid(row=1, column=0, sticky="E")
        tkinter.Label(this, fg=this.font_color, bg=this['bg'], text="Szöveg", font=(this.font_family, 15)).grid(row=2, column=0, sticky="E")
        tkinter.Label(this, fg=this.font_color, bg=this['bg'], text="Plakát", font=(this.font_family, 15)).grid(row=3, column=0, sticky="E")
        this.filename = ""
        this.filename_label = tkinter.Label(this, fg=this.font_color, bg=this['bg'], text="Nincs feltöltött file", font=(this.font_family, 10))
        this.filename_label.grid(row=4, column=1, sticky="NW")

        ttk.Button(this, command=this.upload_poster, text="Feltöltés").grid(row=3, column=1, sticky="W")
        ttk.Button(this, command=this.go_back, text="Vissza").grid(row=6, column=0, sticky="E")
        ttk.Button(this, command=this.insert_ad, text="Felvitel").grid(row=6, column=1, sticky="W")

        this.title = tkinter.Entry(this)
        this.text = tkinter.Entry(this)

        this.title.grid(row=1, column=1, sticky="W")
        this.text.grid(row=2, column=1, sticky='W')

        this.dao = AdDAO()

        this.reset()

    def reset(this) -> None:
        this.filename = ""
        this.filename_label["text"] = "Nincs feltöltött file"
        this.title.delete(0, 'end')
        this.text.delete(0, 'end')

    def upload_poster(this) -> None:
        this.filename = filedialog.askopenfilename()
        if this.filename != "" :
            this.filename_label["text"] = os.path.basename(this.filename)

    def go_back(this) -> None:
        this.master.raise_previous_window()

    def insert_ad(this) -> None:
        if this.title.get() == "" or this.text.get() == "":
            messagebox.showerror("Hiba", "Minden mezőt kötelező kitölteni!")
            return

        # this.dao.insert()