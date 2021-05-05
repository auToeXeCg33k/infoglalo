from .window import Window


class GameWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        print(this.data["duel"])


    def reset(this) -> None:
        pass