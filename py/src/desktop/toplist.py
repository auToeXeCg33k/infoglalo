import tkinter

from .scrollable_window import ScrollableWindow
from ..core.dao.toplist_dao import TopListDAO

# TODO
class ToplistWindow(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)

        this.main_frame.rowconfigure(index=0, weight=1)
        this.main_frame.rowconfigure(index=1, weight=1)
        this.main_frame.rowconfigure(index=2, weight=1)
        this.main_frame.rowconfigure(index=3, weight=1)
        this.main_frame.rowconfigure(index=4, weight=1)
        this.main_frame.rowconfigure(index=5, weight=1)
        this.main_frame.columnconfigure(index=0, weight=1)
        this.main_frame.columnconfigure(index=1, weight=1)
        this.main_frame.columnconfigure(index=2, weight=1)

        this.dao = TopListDAO()
        this.reset()

    def reset(this) -> None:
        for child in this.main_frame.winfo_children():
            child.destroy()

        tkinter.Label(this.main_frame, text="Rangsor").grid(row=0, column=0, columnspan=3, sticky="NESW")
        tkinter.Label(this.main_frame, text="Összesített").grid(row=1, column=0, columnspan=3, sticky="NESW")
        tkinter.Label(this.main_frame, text="Könnyű").grid(row=3, column=0, sticky="NESW")
        tkinter.Label(this.main_frame, text="Közepes").grid(row=3, column=1, sticky="NESW")
        tkinter.Label(this.main_frame, text="Nehéz").grid(row=3, column=2, sticky="NESW")

        tkinter.Button(this.main_frame, command=this.go_back, text="Vissza").grid(row=5, column=0, sticky="NESW")

        aggregated_list = tkinter.Listbox(this.main_frame)
        easy_list = tkinter.Listbox(this.main_frame)
        medium_list = tkinter.Listbox(this.main_frame)
        hard_list = tkinter.Listbox(this.main_frame)

        aggregated_list.grid(row=2, column=0, columnspan=3, sticky="NESW")
        easy_list.grid(row=4, column=0, sticky="NESW")
        medium_list.grid(row=4, column=1, sticky="NESW")
        hard_list.grid(row=4, column=2, sticky="NESW")

        this.show_aggregated(aggregated_list)
        this.show_easy(easy_list)
        this.show_medium(medium_list)
        this.show_hard(hard_list)

    def show_aggregated(this, listbox) -> None:
        data = this.dao.aggregate()
        data.sort(key=lambda l: l['POINTS'], reverse=True)
        data_list = []
        i = 1
        for row in data:
            data_list.append(str(i) + ". " + str(row["USERNAME"]) + "  " + str(row["POINTS"]) + " pont")
            i += 1
        for index, data in enumerate(data_list):
            listbox.insert(index, data)

    def show_easy(this, listbox) -> None:
        data = this.dao.easy()
        data_list = []
        i = 1
        for name, score in data:
            data_list.append(str(i) + ". " + name + "  " + str(score) + " pont")
            i += 1
        for index, data in enumerate(data_list):
            listbox.insert(index, data)


    def show_medium(this, listbox) -> None:
        data = this.dao.medium()
        data_list = []
        i = 1
        for name, score in data:
            data_list.append(str(i) + ". " + name + "  "+ str(score) + " pont")
            i +=1
        for index, data in enumerate(data_list):
            listbox.insert(index, data)

    def show_hard(this, listbox) -> None:
        data = this.dao.hard()
        data_list = []
        i = 1
        for name, score in data:
            data_list.append(str(i) + ". " + name + "  " + str(score) + " pont")
            i += 1
        for index, data in enumerate(data_list):
            listbox.insert(index, data)

    def go_back(this) -> None:
        this.master.raise_previous_window()