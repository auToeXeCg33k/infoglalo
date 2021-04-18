import abc
import tkinter


class Window(tkinter.Frame, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def reset(this):
        pass