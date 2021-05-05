import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
import os

from .window import Window
from ..core.config import ConfigLoader
from ..core.dao.ad_dao import AdDAO

class NewAdsWindow(Window):
    def __init__(this, data):
        Window.__init__(this, data)

        this.rowconfigure(index=0, weight=1)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=300)
        this.rowconfigure(index=4, weight=1)
        this.columnconfigure(index=0, weight=70)
        this.columnconfigure(index=1, weight=30)

        this.font_family = ConfigLoader.get("font-family")
        this.font_color = ConfigLoader.get("font-color")

        tkinter.Label(this, fg=this.font_color, bg=this['bg'], text="Hirdetés felvitele", font=(this.font_family, 25)).grid(row=0, column=0, columnspan=2)
        this.img = None
        this.filename = ""
        this.filename_label = tkinter.Label(this, fg=this.font_color, bg=this['bg'], text="Nincs feltöltött file", font=(this.font_family, 10))
        this.filename_label.grid(row=2, column=1, sticky="NW")

        ttk.Button(this, command=this.upload_poster, text="Feltöltés").grid(row=1, column=1)
        ttk.Button(this, command=this.go_back, text="Vissza").grid(row=4, column=0, sticky="E")
        ttk.Button(this, command=this.insert_ad, text="Felvitel").grid(row=4, column=1, sticky="W")

        this.title = tkinter.Entry(this)
        this.text = tkinter.Entry(this)

        this.title.grid(row=1, column=0, rowspan=2, sticky="NEWS")
        this.text.grid(row=3, column=0, columnspan=2, sticky="NEWS")

        this.dao = AdDAO()

        this.reset()

    def reset(this) -> None:
        this.img = None
        this.filename = ""
        this.filename_label["text"] = "Nincs feltöltött file"
        this.title.delete(0, 'end')
        this.text.delete(0, 'end')
        this.title.insert(0, 'Cím...')
        this.text.insert(0, 'Szöveg...')

    def upload_poster(this) -> None:
        this.filename = filedialog.askopenfilename()

        if this.filename != "" :
            this.filename_label["text"] = os.path.basename(this.filename)
            this.img = Image.open(this.filename)
            img_size = this.img.size
            this.img = this.img.resize((round(300/img_size[1] * img_size[0]), 300))


    def go_back(this) -> None:
        this.master.raise_previous_window()

    def insert_ad(this) -> None:
        if this.title.get() == "" or this.text.get() == "" or this.img is None:
            messagebox.showerror("Hiba", "Minden mezőt kötelező kitölteni!")
            return

        this.dao.insert(this.title.get(), this.text.get(), this.img)
        this.reset()
        this.master.raise_previous_window()