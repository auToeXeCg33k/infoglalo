import tkinter

from .window import Window
from ..core.config import ConfigLoader
from ..core.dao.duel_dao import DuelDAO


class DuelGameWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.dao = DuelDAO()

        font_color = ConfigLoader.get("font-color")
        font_family = ConfigLoader.get("font-family")

        tkinter.Label(master=this, fg=font_color, bg=this["bg"], font=(font_family, 26), text="Párbaj").pack(side=tkinter.TOP, fill=tkinter.X)

        this.question_label = tkinter.Label(master=this, fg=font_color, bg=this["bg"], font=(font_family, 20))
        this.question_label.pack(side=tkinter.TOP, fill=tkinter.X, pady=20)

        answers_frame = tkinter.Frame(master=this, bg=this["bg"])
        answers_frame.pack(side=tkinter.TOP, pady=20)

        for i in range(2):
            answers_frame.rowconfigure(index=i, weight=1)
            answers_frame.columnconfigure(index=i, weight=1)

        this.ans_a_label = tkinter.Label(master=answers_frame, fg=font_color, bg=this["bg"], font=(font_family, 16))
        this.ans_b_label = tkinter.Label(master=answers_frame, fg=font_color, bg=this["bg"], font=(font_family, 16))
        this.ans_c_label = tkinter.Label(master=answers_frame, fg=font_color, bg=this["bg"], font=(font_family, 16))
        this.ans_d_label = tkinter.Label(master=answers_frame, fg=font_color, bg=this["bg"], font=(font_family, 16))

        this.ans_a_label.grid(row=0, column=0, padx=(0, 30))
        this.ans_b_label.grid(row=0, column=1, padx=(30, 0))
        this.ans_c_label.grid(row=1, column=0, padx=(0, 30))
        this.ans_d_label.grid(row=1, column=1, padx=(30, 0))

        this.ans_a_label.bind("<Button-1>", lambda e: this.on_selected("a"))
        this.ans_b_label.bind("<Button-1>", lambda e: this.on_selected("b"))
        this.ans_c_label.bind("<Button-1>", lambda e: this.on_selected("c"))
        this.ans_d_label.bind("<Button-1>", lambda e: this.on_selected("d"))


    def reset(this) -> None:
        this.question_label["text"] = this.data["duel"]["question"]
        this.ans_a_label["text"] = this.data["duel"]["answers"][0]
        this.ans_b_label["text"] = this.data["duel"]["answers"][1]
        this.ans_c_label["text"] = this.data["duel"]["answers"][2]
        this.ans_d_label["text"] = this.data["duel"]["answers"][3]


    def on_selected(this, letter: str) -> None:
        this.dao.add_answer(this.data["duel"]["id"], this.data["user"][0], letter.upper())

        if this.data["duel"]["correct_ans"].lower() == letter:
            print("correct answer")

        else:
            print("bad answer")