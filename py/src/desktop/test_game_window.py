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
        this.accent_color = ConfigLoader.get("accent-color")


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

        tkinter.Label(master=this.setup_frame, bg=this["bg"], fg=font_color, font=(font_family, 26), text="Válassz témakört és nehézséget!").pack(pady=(50, 0))

        this.current_category = tkinter.StringVar(this.setup_frame)
        this.category_menu = tkinter.ttk.Combobox(this.setup_frame, state="readonly", textvariable=this.current_category)
        this.category_menu.pack(pady=(25, 0))

        this.current_difficulty = tkinter.StringVar(this.setup_frame)
        this.difficulty_menu = tkinter.ttk.Combobox(this.setup_frame, state="readonly", textvariable=this.current_difficulty, values=list(this.data["test"]["difficulties"]))
        this.difficulty_menu.pack()

        tkinter.ttk.Button(master=this.setup_frame, command=this.on_options_selected, text="Kezdés").pack(pady=(25, 0))
        tkinter.ttk.Button(master=this.setup_frame, command=this.go_back, text="Vissza").pack(pady=(5, 0))


        # ACTUAL GAME SCREEN
        this.game_frame = tkinter.Frame(this, bg=this["bg"])
        this.question_no_label = tkinter.Label(this.game_frame, font=(font_family, 26), fg=font_color, bg=this["bg"])
        this.question_label = tkinter.Label(this.game_frame, font=(font_family, 24, tkinter.UNDERLINE), fg=font_color, bg=this["bg"])
        this.answers_frame = tkinter.Frame(this.game_frame, bg=this["bg"])

        this.question_no_label.pack(pady=(50, 0))
        this.question_label.pack(pady=(15, 0))
        this.answers_frame.pack(pady=(15, 0))

        for i in range(2):
            this.answers_frame.rowconfigure(i, weight=1)
            this.answers_frame.columnconfigure(i, weight=1)

        this.ans_a_label = tkinter.Label(this.answers_frame, bg=this["bg"], fg=font_color, font=(font_family, 20))
        this.ans_b_label = tkinter.Label(this.answers_frame, bg=this["bg"], fg=font_color, font=(font_family, 20))
        this.ans_c_label = tkinter.Label(this.answers_frame, bg=this["bg"], fg=font_color, font=(font_family, 20))
        this.ans_d_label = tkinter.Label(this.answers_frame, bg=this["bg"], fg=font_color, font=(font_family, 20))

        this.ans_a_label.grid(row=0, column=0, padx=(0, 10))
        this.ans_b_label.grid(row=0, column=1, padx=(10, 0))
        this.ans_c_label.grid(row=1, column=0, padx=(0, 10), pady=(10, 0))
        this.ans_d_label.grid(row=1, column=1, padx=(10, 0), pady=(10, 0))

        this.ans_a_label.bind("<Button-1>", lambda e: this.on_answer_selected('a'))
        this.ans_b_label.bind("<Button-1>", lambda e: this.on_answer_selected('b'))
        this.ans_c_label.bind("<Button-1>", lambda e: this.on_answer_selected('c'))
        this.ans_d_label.bind("<Button-1>", lambda e: this.on_answer_selected('d'))

        this.ans_a_label.bind("<Enter>", lambda e: this.on_mouse_enter(this.ans_a_label))
        this.ans_b_label.bind("<Enter>", lambda e: this.on_mouse_enter(this.ans_b_label))
        this.ans_c_label.bind("<Enter>", lambda e: this.on_mouse_enter(this.ans_c_label))
        this.ans_d_label.bind("<Enter>", lambda e: this.on_mouse_enter(this.ans_d_label))

        this.ans_a_label.bind("<Leave>", lambda e: this.on_mouse_leave(this.ans_a_label))
        this.ans_b_label.bind("<Leave>", lambda e: this.on_mouse_leave(this.ans_b_label))
        this.ans_c_label.bind("<Leave>", lambda e: this.on_mouse_leave(this.ans_c_label))
        this.ans_d_label.bind("<Leave>", lambda e: this.on_mouse_leave(this.ans_d_label))


        # RESULTS SCREEN
        this.results_frame = tkinter.Frame(this, bg=this["bg"])
        tkinter.Label(this.results_frame, fg=font_color, font=(font_family, 26), bg=this["bg"], text="Eredmények").pack()

        this.answer_correctness_labels: list[tkinter.Label] = list()

        for i in range(this.num_max_questions):
            this.answer_correctness_labels.append(tkinter.Label(this.results_frame, bg=this["bg"], fg=font_color, font=(font_family, 20)))
            this.answer_correctness_labels[-1].pack()

        tkinter.ttk.Button(master=this.results_frame, command=this.go_back, text="Vissza").pack()



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
        this.given_answers.append(letter == this.data["test"]["tests"][this.question_index]["correct_ans"].lower())

        answer_text = ""
        for letter2, text in this.data["test"]["tests"][this.question_index]["answers"]:
            if letter2.lower() == letter.lower():
                answer_text = text
                break

        this.dao.add_answer(this.data["user"][0], this.data["test"]["tests"][this.question_index]["question"], letter.upper(), answer_text)

        if this.question_index + 1 < this.num_max_questions:
            this.on_next_question()
        else:
            this.on_game_end()


    def on_next_question(this) -> None:
        this.question_index += 1

        this.question_no_label["text"] = str(this.question_index + 1) + ". kérdés"
        this.question_label["text"] = this.data["test"]["tests"][this.question_index]["question"]
        this.ans_a_label["text"] = this.data["test"]["tests"][this.question_index]["answers"][0][0] + ": " + this.data["test"]["tests"][this.question_index]["answers"][0][1]
        this.ans_b_label["text"] = this.data["test"]["tests"][this.question_index]["answers"][1][0] + ": " + this.data["test"]["tests"][this.question_index]["answers"][1][1]
        this.ans_c_label["text"] = this.data["test"]["tests"][this.question_index]["answers"][2][0] + ": " + this.data["test"]["tests"][this.question_index]["answers"][2][1]
        this.ans_d_label["text"] = this.data["test"]["tests"][this.question_index]["answers"][3][0] + ": " + this.data["test"]["tests"][this.question_index]["answers"][3][1]


    def on_game_end(this) -> None:
        this.setup_frame.pack_forget()
        this.game_frame.pack_forget()
        this.results_frame.pack()

        for i in range(len(this.answer_correctness_labels)):
            this.answer_correctness_labels[i]["text"] = str(i + 1) + ". " + ("Helyes" if this.given_answers[i] else "Helytelen")

    def on_mouse_enter(this, label: tkinter.Label) -> None:
        label["bg"]=this.accent_color

    def on_mouse_leave(this, label: tkinter.Label) -> None:
        label["bg"]=this["bg"]