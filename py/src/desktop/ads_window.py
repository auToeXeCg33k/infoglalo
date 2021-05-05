import tkinter
import tkinter
from tkinter import messagebox
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

        tkinter.Label(this, fg=this.font_color, text="Hirdetések", bg=this['bg'], font=(this.font_family, 25))

        this.dao = AdDAO()

        this.reset()

    def reset(this) -> None:
        for child in this.main_frame.winfo_children():
            child.destroy()

        ttk.Button(this.main_frame, text="Vissza", command=this.go_back).place(x=10, y=10)
        if this.data["user"][4]:  # ha admin
             ttk.Button(this.main_frame, text="Hirdetés felvitele", command=this.go_admin).place(x=800, y=10)

        dao = AdDAO()
        data = dao.find_all()
        for i in range (len(data)):
            img_button = ttk.Button(this.main_frame, image=data[i][2], command=lambda index=i: this.get_info(data, index))
            img_button.image = data[i][2]
            img_button.place(x=110, y=((len(data)-1) * 330) + 10 - i * 330)
            ttk.Button(this.main_frame, text="X", command=lambda index=i: this.delete_ad(index)).place(x=110 + data[i][2].width() + 10, y=((len(data)-1) * 330) + 10 - i * 330)

    def get_info(this, data, i) -> None:
        info_frame = tkinter.Toplevel()
        info_frame.columnconfigure(index=0, weight=1)
        info_frame.rowconfigure(index=0, weight=1)
        info_frame.rowconfigure(index=1, weight=0)
        tkinter.Label(info_frame, fg=this.font_color, text=data[i][0], bg=this['bg'], font=(this.font_family, 25)).grid(row=0, column=0, sticky="NESW")
        tkinter.Label(info_frame, fg=this.font_color, text=data[i][1], bg=this['bg'], font=(this.font_family, 15)).grid(row=1, column=0, sticky="NESW")

    def delete_ad(this, index) -> None:
        msgbox = tkinter.messagebox.askquestion('Hirdetés törlése', 'Biztosan ki szeretnéd törölni a hirdetést?',
                                           icon='warning')

        if msgbox == 'yes':
            this.dao.delete(index)

        this.reset()

    def go_back(this) -> None:
        this.master.raise_previous_window()

    def go_admin(this) -> None:
        this.master.raise_window(NewAdsWindow)


