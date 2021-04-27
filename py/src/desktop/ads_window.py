import tkinter as tk
import tkinter.messagebox
from .scrollable_window import ScrollableWindow
from ..core.dao.ad_dao import AdDAO


class AdsWindow(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)
        this.reset()
        tk.Label(this, text="Hirdetések", font=(None, 25)).grid(row=0, column=0, sticky="NESW")
        
    def reset(this) -> None:
        for child in this.main_frame.winfo_children():
            child.destroy()

        dao = AdDAO()
        data = dao.find_all()
        for i in range (len(data)):
            this.main_frame.rowconfigure(index=i, weight=1)
            img_button = tk.Button(this.main_frame, image=data[i][2], command=lambda index=i: this.get_info(data, index))
            img_button.image = data[i][2]
            img_button.grid(row=i, column=0, sticky="NEWS")


    def get_info(this, data, i):
        info_frame = tk.Toplevel()
        info_frame.columnconfigure(index=0, weight=1)
        info_frame.rowconfigure(index=0, weight=1)
        info_frame.rowconfigure(index=1, weight=0)
        tk.Label(info_frame, text=data[i][0], font=(None, 25)).grid(row=0, column=0, sticky="NESW")
        tk.Label(info_frame, text=data[i][1], font=(None, 15)).grid(row=1, column=0, sticky="NESW")


