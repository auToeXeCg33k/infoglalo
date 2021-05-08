import tkinter
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

from .window import Window
from ..core.config import ConfigLoader
from ..core.dao.stat_dao import StatDAO
from ..core.dao.toplist_dao import TopListDAO

class StatWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.font_family = ConfigLoader.get("font-family")
        this.font_color = ConfigLoader.get("font-color")


        this.rowconfigure(index=0, weight=30)
        this.rowconfigure(index=1, weight=20)
        this.rowconfigure(index=2, weight=30)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=20)
        this.columnconfigure(index=0, weight=1)
        this.columnconfigure(index=1, weight=1)

        tkinter.Label(this, fg=this.font_color, text="Statisztikák", bg=this['bg'],
                      font=(this.font_family, 25)).grid(row=0, column=0, columnspan=2)

        tkinter.Label(this, fg=this.font_color, text="Összesített korosztályos statisztika", bg=this['bg'],
                      font=(this.font_family, 18)).grid(row=1, column=0)

        tkinter.Label(this, fg=this.font_color, text=this.data["user"][0] + " témakör szerinti statisztikája", bg=this['bg'],
                      font=(this.font_family, 18)).grid(row=1, column=1)

        ttk.Button(this, text="Mutat", command=this.show_ages_stat).grid(row=2, column=0, sticky="N")
        ttk.Button(this, text="Mutat", command=this.show_theme_stat).grid(row=2, column=1, sticky="N")

        ttk.Button(this, text="Vissza", command=this.go_back).grid(row=3, column=0)


    def reset(this) -> None:
        pass

    def show_ages_stat(this) -> None:
        this.dao = TopListDAO()
        data = this.dao.aggregate()

        points = list()
        for row in data:
            points.append(int(row["POINTS"]))


        this.dao = StatDAO()
        data = this.dao.get_age_stat()

        ages = list()
        for row in data:
            ages.append(int(row[0]))

        first = list()
        sec = list()
        third = list()
        for i in range(len(ages)):
            if ages[i] < 18:
                first.append(points[i])
            elif ages[i] < 50:
                sec.append(points[i])
            else:
                third.append(points[i])

        fig = plt.figure(figsize=(7, 5))

        ypos = np.arange(3)
        categories = ["<18", "18-50", "50<"]
        plt.xticks(ypos, categories)
        plt.ylabel("Pont")

        plt.bar(ypos, [sum(first)/len(first), sum(sec)/len(sec), sum(third)/len(third) ])

        plt.show()

    def show_theme_stat(this) -> None:
        this.dao = StatDAO()
        data = this.dao.get_user_theme(this.data["user"][0])

        categories = list ()
        values = list()

        for row in data:
            categories.append(row[0])
            values.append(row[1])

        ypos = np.arange(len(categories))
        plt.xticks(ypos, categories)
        plt.ylabel("Helyes válaszok száma")

        plt.bar(ypos, values)

        plt.show()

    def go_back(this) -> None:
        this.master.raise_previous_window()