import tkinter
from window import Window

class MainMenuWindow(Window):
    def __init__(this):
        Window.__init__(this)

        this.rowconfigure(index=0, weight=1)
        this.rowconfigure(index=1, weight=1)
        this.rowconfigure(index=2, weight=1)
        this.rowconfigure(index=3, weight=1)
        this.rowconfigure(index=4, weight=1)
        this.rowconfigure(index=5, weight=1)
        this.columnconfigure(index=0, weight=1)

        this.reset()

    def reset(this) -> None:
        #MENU TITLE
        tkinter.Label(this, text="Menü", font=(None, 25)).grid(row=0, column=0, sticky="NESW")

        #MENU BUTTONS
        tkinter.Button(this, command=this.go_to_play, text="Játék").grid(row=1, column=0, sticky="NESW")
        tkinter.Button(this, command=this.go_to_ranking, text="Rangsor").grid(row=2, column=0, sticky="NESW")
        tkinter.Button(this, command=this.go_to_social, text="Közösségi").grid(row=3, column=0, sticky="NESW")
        tkinter.Button(this, command=this.go_to_ad, text="Hirdetések").grid(row=4, column=0, sticky="NESW")
        tkinter.Button(this, command=this.go_to_settings, text="Beállítások").grid(row=5, column=0, sticky="NESW")

    def go_to_play():
        pass

    def go_to_ranking():
        pass

    def go_to_social():
        pass

    def go_to_ad():
        pass

    def go_to_settings():
        pass