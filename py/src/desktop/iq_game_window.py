import tkinter
from tkinter import ttk

from .window import Window
from ..core.config import ConfigLoader
from ..core.dao.iq_dao import IQDAO

class IQWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        this.dao = IQDAO()
        this.data["iq"] = dict()


        this.question_index = 0
        this.num_max_questions = 5
        this.given_answers: list[bool] = list()

        font_color = ConfigLoader.get("font-color")
        font_family = ConfigLoader.get("font-family")

        tkinter.Label(master=this, fg=font_color, bg=this["bg"], font=(font_family, 26), text="IQ teszt").pack(
            side=tkinter.TOP, fill=tkinter.X)

        # ACTUAL GAME SCREEN
        this.game_frame = tkinter.Frame(this, bg=this["bg"])
        this.question_label = tkinter.Label(this.game_frame, font=(font_family, 11), fg=font_color, bg=this["bg"])
        this.answers_frame = tkinter.Frame(this.game_frame, bg=this["bg"])

        this.question_label.pack()
        this.answers_frame.pack()

        for i in range(2):
            this.answers_frame.rowconfigure(index=i, weight=1)
            this.answers_frame.columnconfigure(index=i, weight=1)

        this.ans_a_label = tkinter.Label(master=this.answers_frame, fg=font_color, bg=this["bg"],
                                         font=(font_family, 16))
        this.ans_b_label = tkinter.Label(master=this.answers_frame, fg=font_color, bg=this["bg"],
                                         font=(font_family, 16))
        this.ans_c_label = tkinter.Label(master=this.answers_frame, fg=font_color, bg=this["bg"],
                                         font=(font_family, 16))
        this.ans_d_label = tkinter.Label(master=this.answers_frame, fg=font_color, bg=this["bg"],
                                         font=(font_family, 16))

        this.ans_a_label.grid(row=0, column=0, padx=(0, 30))
        this.ans_b_label.grid(row=0, column=1, padx=(30, 0))
        this.ans_c_label.grid(row=1, column=0, padx=(0, 30))
        this.ans_d_label.grid(row=1, column=1, padx=(30, 0))

        this.ans_a_label.bind("<Button-1>", lambda e: this.on_answer_selected("a"))
        this.ans_b_label.bind("<Button-1>", lambda e: this.on_answer_selected("b"))
        this.ans_c_label.bind("<Button-1>", lambda e: this.on_answer_selected("c"))
        this.ans_d_label.bind("<Button-1>", lambda e: this.on_answer_selected("d"))

        # RESULTS SCREEN
        this.results_frame = tkinter.Frame(this, bg=this["bg"])
        tkinter.Label(this.results_frame, fg=font_color, font=(font_family, 26), bg=this["bg"],
                      text="Eredmények").pack()

        this.answer_correctness_labels: list[tkinter.Label] = list()

        for i in range(this.num_max_questions):
            this.answer_correctness_labels.append(
                tkinter.Label(this.results_frame, bg=this["bg"], fg=font_color, font=(font_family, 20)))
            this.answer_correctness_labels[-1].pack()

        this.iq_level_label = tkinter.Label(this.results_frame, bg=this["bg"], fg=font_color, font=(font_family, 20))
        this.iq_level_label.pack()
        tkinter.ttk.Button(master=this.results_frame, command=this.go_back, text="Vissza").pack()

        this.start()

    def reset(this) -> None:
        this.given_answers.clear()
        this.question_index = -1

        this.start()

    def start(this) -> None:
        this.results_frame.pack_forget()
        this.game_frame.pack()

        this.data["iq"]["tests"] = this.dao.get_questions()

        this.on_next_question()

    def on_next_question(this) -> None:
        this.question_index += 1


        this.question_label["text"] = this.data["iq"]["tests"][this.question_index]["question"]
        this.ans_a_label["text"] = this.data["iq"]["tests"][this.question_index]["answers"][0][0] + ": " + \
                                   this.data["iq"]["tests"][this.question_index]["answers"][0][1]
        this.ans_b_label["text"] = this.data["iq"]["tests"][this.question_index]["answers"][1][0] + ": " + \
                                   this.data["iq"]["tests"][this.question_index]["answers"][1][1]
        this.ans_c_label["text"] = this.data["iq"]["tests"][this.question_index]["answers"][2][0] + ": " + \
                                   this.data["iq"]["tests"][this.question_index]["answers"][2][1]
        this.ans_d_label["text"] = this.data["iq"]["tests"][this.question_index]["answers"][3][0] + ": " + \
                                   this.data["iq"]["tests"][this.question_index]["answers"][3][1]


    def on_answer_selected(this, letter: str) -> None:
        this.given_answers.append(letter == this.data["iq"]["tests"][this.question_index]["correct_ans"].lower())

        if this.question_index + 1 < this.num_max_questions:
            this.on_next_question()
        else:
            this.on_game_end()

    def on_game_end(this) -> None:
        this.game_frame.pack_forget()
        this.results_frame.pack()

        correct = 0
        for i in range(len(this.answer_correctness_labels)):
            this.answer_correctness_labels[i]["text"] = str(i + 1) + ". " + ("Helyes" if this.given_answers[i] else "Helytelen")
            if this.given_answers[i]: correct += 1

        this.iq_level_label["text"] = "A teszt alapján az iq szinted " + str(round(70 + 140/this.num_max_questions * correct))

    def go_back(this) -> None:
        this.master.raise_previous_window()