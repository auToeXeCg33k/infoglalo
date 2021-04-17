import tkinter


class App(tkinter.Tk):
    def __init__(this, *args, **kwargs):
        tkinter.Tk.__init__(this, *args, **kwargs)
        this.title()
        print("Hello, World!")