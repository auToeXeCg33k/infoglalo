import tkinter
import tkinter.ttk
from datetime import datetime, timedelta

from core.config import ConfigLoader
from core.dao.comp_dao import CompDAO
from core.dao.duel_dao import DuelDAO
from .window import Window


class CompGameWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.dao = DuelDAO()
        this.c_dao = CompDAO()

        font_color = ConfigLoader.get("font-color")
        font_family = ConfigLoader.get("font-family")
        this.accent_color = ConfigLoader.get("accent-color")

        tkinter.Label(master=this, fg=font_color, bg=this["bg"], font=(font_family, 26), text="Verseny").pack(side=tkinter.TOP, fill=tkinter.X)

        this.question_label = tkinter.Label(master=this, fg=font_color, bg=this["bg"], font=(font_family, 20))

        this.answers_frame = tkinter.Frame(master=this, bg=this["bg"])

        for i in range(2):
            this.answers_frame.rowconfigure(index=i, weight=1)
            this.answers_frame.columnconfigure(index=i, weight=1)

        this.ans_a_label = tkinter.Label(master=this.answers_frame, fg=font_color, bg=this["bg"], font=(font_family, 16))
        this.ans_b_label = tkinter.Label(master=this.answers_frame, fg=font_color, bg=this["bg"], font=(font_family, 16))
        this.ans_c_label = tkinter.Label(master=this.answers_frame, fg=font_color, bg=this["bg"], font=(font_family, 16))
        this.ans_d_label = tkinter.Label(master=this.answers_frame, fg=font_color, bg=this["bg"], font=(font_family, 16))

        this.ans_a_label.grid(row=0, column=0, padx=(0, 30))
        this.ans_b_label.grid(row=0, column=1, padx=(30, 0))
        this.ans_c_label.grid(row=1, column=0, padx=(0, 30))
        this.ans_d_label.grid(row=1, column=1, padx=(30, 0))

        this.ans_a_label.bind("<Button-1>", lambda e: this.on_selected("a"))
        this.ans_b_label.bind("<Button-1>", lambda e: this.on_selected("b"))
        this.ans_c_label.bind("<Button-1>", lambda e: this.on_selected("c"))
        this.ans_d_label.bind("<Button-1>", lambda e: this.on_selected("d"))

        this.ans_a_label.bind("<Enter>", lambda e: this.on_mouse_enter(this.ans_a_label))
        this.ans_b_label.bind("<Enter>", lambda e: this.on_mouse_enter(this.ans_b_label))
        this.ans_c_label.bind("<Enter>", lambda e: this.on_mouse_enter(this.ans_c_label))
        this.ans_d_label.bind("<Enter>", lambda e: this.on_mouse_enter(this.ans_d_label))

        this.ans_a_label.bind("<Leave>", lambda e: this.on_mouse_leave(this.ans_a_label))
        this.ans_b_label.bind("<Leave>", lambda e: this.on_mouse_leave(this.ans_b_label))
        this.ans_c_label.bind("<Leave>", lambda e: this.on_mouse_leave(this.ans_c_label))
        this.ans_d_label.bind("<Leave>", lambda e: this.on_mouse_leave(this.ans_d_label))

        this.result_frame = tkinter.Frame(master=this, bg=this["bg"])
        this.correctness_label = tkinter.Label(master=this.result_frame, fg=font_color, bg=this["bg"], font=(font_family, 20))
        this.result_label = tkinter.Label(master=this.result_frame, fg=font_color, bg=this["bg"], font=(font_family, 14))
        tkinter.ttk.Button(master=this.result_frame, text="Vissza", command=this.go_back).pack(side=tkinter.BOTTOM)

        this.correctness_label.pack()
        this.result_label.pack()


    def reset(this) -> None:
        this.result_frame.pack_forget()
        this.question_label.pack(side=tkinter.TOP, fill=tkinter.X, pady=20)
        this.answers_frame.pack(side=tkinter.TOP, pady=20)

        this.question_label["text"] = this.data["comp"]["szoveg"]
        this.ans_a_label["text"] = this.data["comp"]["answers"][0][0] + ": " + this.data["comp"]["answers"][0][1]
        this.ans_b_label["text"] = this.data["comp"]["answers"][1][0] + ": " + this.data["comp"]["answers"][1][1]
        this.ans_c_label["text"] = this.data["comp"]["answers"][2][0] + ": " + this.data["comp"]["answers"][2][1]
        this.ans_d_label["text"] = this.data["comp"]["answers"][3][0] + ": " + this.data["comp"]["answers"][3][1]


    def on_selected(this, letter: str) -> None:
        this.c_dao.add_answer(this.data["comp"]["szoveg"], this.data["user"][0],this.data["comp"]["ans"][0][0],letter.upper())

        this.question_label.pack_forget()
        this.answers_frame.pack_forget()

        this_is_correct = this.data["comp"]["jel"].lower() == letter
        this.correctness_label["text"] = "A válaszod helyes volt!" if this_is_correct else "A válaszod helytelen volt."

        this.c_dao.delete_utkozet(this.data["comp"]["comp_id"], this.data["user"][0])

        if this_is_correct:
            date = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
            this.c_dao.join_play(this.data["comp"]["comp_id"], this.data["user"][0], date)
        this.result_frame.pack(side=tkinter.TOP, pady=50)


    def go_back(this) -> None:
        this.master.raise_previous_window()

    def on_mouse_enter(this, label: tkinter.Label) -> None:
        label["bg"]=this.accent_color

    def on_mouse_leave(this, label: tkinter.Label) -> None:
        label["bg"]=this["bg"]