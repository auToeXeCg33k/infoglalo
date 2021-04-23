import abc
import tkinter


class Window(tkinter.Frame, metaclass=abc.ABCMeta):
    def __init__(this, data, *args, **kwargs):
        tkinter.Frame.__init__(this, *args, **kwargs)
        this.data = data


    @abc.abstractmethod
    def reset(this) -> None:
        pass