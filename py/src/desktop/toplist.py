from .scrollable_window import ScrollableWindow

class ToplistWindow(ScrollableWindow):
    def __init__(this, data) -> None:
        ScrollableWindow.__init__(this, data)
        this.reset()

    def reset(this) -> None:
        pass
