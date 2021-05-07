import tkinter
import tkinter.ttk

from .window import Window
from ..core.dao.test_dao import TestDAO
from ..core.config import ConfigLoader


class TestGameWindow(Window):
    def __init__(this, data) -> None:
        Window.__init__(this, data)

        font_color = ConfigLoader.get("font-color")
        font_family = ConfigLoader.get("font-family")


        this.dao = TestDAO()
        this.data["test"] = dict()
        this.data["test"]["categories"]: list[str] = list()
        this.data["test"]["difficulties"]: dict[str, int] = {
            "Könnyű": 0,
            "Közepes": 1,
            "Nehéz": 2
        }

        # THIS REFERS TO THE CURRENT QUESTION
        this.question_index = 0
        this.num_max_questions = 3


        # STORE ANSWER CORRECTNESS
        this.given_answers: list[bool] = list()


        # INITIAL SETUP SCREEN
        this.setup_frame = tkinter.Frame(this, bg=this["bg"])

        this.current_category = tkinter.StringVar(this.setup_frame)
        this.category_menu = tkinter.ttk.Combobox(this.setup_frame, state="readonly", textvariable=this.current_category)
        this.category_menu.pack()

        this.current_difficulty = tkinter.StringVar(this.setup_frame)
        this.difficulty_menu = tkinter.ttk.Combobox(this.setup_frame, state="readonly", textvariable=this.current_difficulty, values=list(this.data["test"]["difficulties"]))
        this.difficulty_menu.pack()

        tkinter.ttk.Button(master=this.setup_frame, command=this.on_options_selected, text="Kezdés").pack()
        tkinter.ttk.Button(master=this.setup_frame, command=this.go_back, text="Vissza").pack()


        # ACTUAL GAME SCREEN
        this.game_frame = tkinter.Frame(this, bg=this["bg"])
        this.question_label = tkinter.Label(this.game_frame, font=(font_family, 24), fg=font_color, bg=this["bg"])
        this.answers_frame = tkinter.Frame(this.game_frame, bg=this["bg"])

        this.question_label.pack()
        this.answers_frame.pack()

        for i in range(2):
            this.answers_frame.rowconfigure(i, weight=1)
            this.answers_frame.columnconfigure(i, weight=1)

        this.ans_a_label = tkinter.Label(this.answers_frame, bg=this["bg"], fg=font_color, font=(font_family, 20))
        this.ans_b_label = tkinter.Label(this.answers_frame, bg=this["bg"], fg=font_color, font=(font_family, 20))
        this.ans_c_label = tkinter.Label(this.answers_frame, bg=this["bg"], fg=font_color, font=(font_family, 20))
        this.ans_d_label = tkinter.Label(this.answers_frame, bg=this["bg"], fg=font_color, font=(font_family, 20))

        this.ans_a_label.grid(row=0, column=0)
        this.ans_b_label.grid(row=0, column=1)
        this.ans_c_label.grid(row=1, column=0)
        this.ans_d_label.grid(row=1, column=1)

        this.ans_a_label.bind("<Button-1>", lambda e: this.on_answer_selected('a'))
        this.ans_b_label.bind("<Button-1>", lambda e: this.on_answer_selected('b'))
        this.ans_c_label.bind("<Button-1>", lambda e: this.on_answer_selected('c'))
        this.ans_d_label.bind("<Button-1>", lambda e: this.on_answer_selected('d'))


        # RESULTS SCREEN
        this.results_frame = tkinter.Frame(this, bg=this["bg"])



    def reset(this) -> None:
        this.data["test"]["categories"].clear()
        this.data["test"]["categories"].extend(this.dao.get_categories())

        this.given_answers.clear()

        this.current_category.set(this.data["test"]["categories"][0])
        this.category_menu["values"] = this.data["test"]["categories"]

        this.current_difficulty.set(list(this.data["test"]["difficulties"])[0])

        this.question_index = -1

        this.game_frame.pack_forget()
        this.results_frame.pack_forget()
        this.setup_frame.pack()


    def go_back(this) -> None:
        this.master.raise_previous_window()


    def on_options_selected(this) -> None:
        this.setup_frame.pack_forget()
        this.results_frame.pack_forget()
        this.game_frame.pack()

        this.data["test"]["tests"] = this.dao.get_question_series(this.data["test"]["difficulties"][this.current_difficulty.get()], this.current_category.get(), 3)

        this.on_next_question()


    def on_answer_selected(this, letter: str) -> None:
        # TODO
        print("correct" if letter == this.data["test"]["tests"][this.question_index]["correct_ans"].lower() else "incorrect")

        if this.question_index + 1 < this.num_max_questions:
            this.on_next_question()
        else:
            this.on_game_end()


    def on_next_question(this) -> None:
        this.question_index += 1

        this.question_label["text"] = this.data["test"]["tests"][this.question_index]["question"]
        this.ans_a_label["text"] = this.data["test"]["tests"][this.question_index]["answers"][0]
        this.ans_b_label["text"] = this.data["test"]["tests"][this.question_index]["answers"][1]
        this.ans_c_label["text"] = this.data["test"]["tests"][this.question_index]["answers"][2]
        this.ans_d_label["text"] = this.data["test"]["tests"][this.question_index]["answers"][3]


    def on_game_end(this) -> None:
        # TODO
        this.setup_frame.pack_forget()
        this.game_frame.pack_forget()
        this.results_frame.pack()
        print("the end")