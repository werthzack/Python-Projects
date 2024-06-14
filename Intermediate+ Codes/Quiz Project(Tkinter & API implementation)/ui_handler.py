import html
import random
import data
from question_model import *
from tkinter import *
from quiz_brain import QuizBrain
from tkinter import ttk, PhotoImage, messagebox


class Window:
    def __init__(self):
        self.in_question = None
        self.correct_answer = None
        self.active = False
        self.quiz_parameters = {}
        self.question_bank = []
        self.home()

    def load(self):
        self.question_bank.clear()
        data.load_data(self.quiz_parameters["amount"], self.quiz_parameters["difficulty"],
                       self.quiz_parameters["type"], self.quiz_parameters["id"])
        amount = self.quiz_parameters["amount"]
        print(len(data.question_data), amount)
        if len(data.question_data) < amount:
            messagebox.showinfo(title="Notification", message="Could not find any questions under the "
                                                              "selected parameters in the API at the moment😢")
            self.home()
            return
        self.active = True
        for info in data.question_data:
            new_question = Question(info["question"], info["correct_answer"], info["category"],
                                    info["incorrect_answers"])
            self.question_bank.append(new_question)

        quiz_brain = QuizBrain(self.question_bank, self.quiz_parameters["type"])
        self.quiz_window(quiz_brain)

    def home(self):
        def check_details():
            try:
                if not 3 <= question_amount.get() <= 50:
                    if question_amount.get() > 50:
                        messagebox.showinfo(title="Out of Range", message="Question amount has exceeded maximum range, "
                                                                          "setting it to 50")
                        question_amount.set(50)
                    else:
                        messagebox.showinfo(title="Out of Range", message="Question amount does not exceed the minimum "
                                                                          "range, setting it to 3")
                        question_amount.set(3)
                chosen_id = next(
                    (category["id"] for category in category_data if category["name"] == selected_category.get()), "")
                difficulty = selected_difficulty.get().lower()
                if difficulty == "any":
                    difficulty = ""
                self.quiz_parameters["amount"] = question_amount.get()
                self.quiz_parameters["difficulty"] = difficulty
                self.quiz_parameters["type"] = selected_type.get()
                self.quiz_parameters["id"] = chosen_id
                window.destroy()
                self.load()

            except (ValueError, TclError):
                messagebox.showinfo(title="Error", message="Invalid data type for Questions, should be an integer")

        category_data = data.get_categories()
        background = "#0A1E56"
        font = ("Cambria", 16, "bold")
        window = Tk()
        window.title("Home")
        window.config(bg=background, padx=40, pady=20)

        selected_difficulty = StringVar()
        selected_category = StringVar()
        question_amount = IntVar()

        canvas = Canvas(width=200, height=200, highlightthickness=0, background="yellow")
        canvas.create_text(100, 100, text="TRIVIA QUIZ", font=("Cambria", 40, "bold"), width=180, justify="center")
        canvas.grid(row=0, column=0, columnspan=2)

        # Labels
        question_label = Label(text="Questions:", bg=background, fg="white", font=font)
        question_label.grid(row=1, column=0)
        difficulty_label = Label(text="Difficulty:", bg=background, fg="white", font=font)
        difficulty_label.grid(row=2, column=0)
        category_label = Label(text="Category:", bg=background, fg="white", font=font)
        category_label.grid(row=3, column=0)
        type_label = Label(text="Question Type:", bg=background, fg="white", font=font)
        type_label.grid(row=4, column=0)

        # Variables
        question_amount.set(10)
        difficulty_options = ["Any", "Easy", "Medium", "Hard"]
        selected_type = StringVar()
        selected_type.set("boolean")
        category_options = [category["name"] for category in category_data]
        category_options.insert(0, "Any")

        # Entries and Options
        question_entry = ttk.Spinbox(from_=3, to=50, increment=1, textvariable=question_amount, width=10)
        question_entry.grid(row=1, column=1, sticky="EW")
        difficulty_entry = ttk.OptionMenu(window, selected_difficulty, difficulty_options[0],
                                          *difficulty_options)
        difficulty_entry.grid(row=2, column=1, sticky="EW")
        category_entry = ttk.OptionMenu(window, selected_category, category_options[0],
                                        *category_options)
        category_entry.grid(row=3, column=1, sticky="EW")
        tf_option = ttk.Radiobutton(window, text="True/False", value="boolean",
                                    variable=selected_type)
        tf_option.grid(row=4, column=1, pady=5, sticky="EW")
        mc_option = ttk.Radiobutton(window, text="Multiple Choice", value="multiple",
                                    variable=selected_type)
        mc_option.grid(row=5, column=1, pady=5, sticky="EW")

        start_button = Button(text="Take Quiz", font=("Cambria", 12, "normal"), command=check_details)
        start_button.grid(row=6, column=0, columnspan=2, pady=10)

        window.resizable(False, False)
        window.eval(f'tk::PlaceWindow {window.winfo_pathname(window.winfo_id())} center')

        window.mainloop()

    def quiz_window(self, brain):
        self.correct_answer = ""
        self.in_question = False

        def check(answer: str):
            if self.in_question is False:
                return
            self.in_question = False
            if quiz.check_answer(html.escape(answer)):
                canvas.config(bg="green")
            else:
                canvas.config(bg="dark red")
            if quiz.quiz_type == "multiple":
                for i in range(4):
                    if option_vars[i].get() == self.correct_answer:
                        options[i].config(bg="green")
            score_label.config(text=f"Score: {quiz.score}")
            window.after(2000, get_next_question)

        def retry():
            window.destroy()
            self.load()

        def menu():
            window.destroy()
            self.home()

        def get_next_question():
            canvas.config(bg="white")
            if quiz.still_has_questions():
                q_text = quiz.next_question()
                if quiz.quiz_type == "multiple":
                    q_options, correct_ans = quiz.get_options()
                    q_options.append(correct_ans)
                    print(correct_ans)
                    self.correct_answer = html.unescape(correct_ans)
                    random.shuffle(q_options)
                    for i in range(4):
                        option_vars[i].set(html.unescape(q_options[i]))
                        options[i].config(bg="white")
                canvas.itemconfig(question_text, text=q_text)
                self.in_question = True
            else:
                percentage = (quiz.score / quiz.question_number) * 100
                if percentage > 80:
                    comments = "Great Work!"
                elif percentage > 60:
                    comments = "Keep Going!"
                else:
                    comments = "Aim Higher!"

                end_text = (f"The Quiz has been completed,"
                            f" You scored {quiz.score} out of {quiz.question_number} questions"
                            f" Your percentage is {round(percentage)}%, {comments}")
                canvas.itemconfig(question_text, text=end_text)
                if quiz.quiz_type == "boolean":
                    true_button.grid_forget()
                    false_button.grid_forget()
                else:
                    [option.grid_forget() for option in options]

                menu_button.grid(row=2, column=1, sticky="")
                retry_button.grid(row=2, column=0)

        window = Tk()
        window.title("Quiz")
        window.config(bg="blue", padx=40, pady=20)

        quiz = brain
        score_label = Label(text="Score: 0", fg="white", bg="blue", font=("Cambria", 20, "bold"))
        score_label.grid(row=0, column=1, sticky="E")

        canvas = Canvas(width=400, height=300, background="white", highlightthickness=0)
        question_text = canvas.create_text(
            200,
            150,
            text="Some Question",
            font=("Cambria", 18, "italic"),
            width=380
        )
        canvas.grid(row=1, column=0, columnspan=2, pady=30)

        menu_button = Button(text="Menu", font=("Cambria", 18, "normal"), command=menu)
        menu_button.grid(row=0, column=0, sticky="W")
        retry_button = Button(text="Retry", font=("Cambria", 18, "normal"), command=retry)

        if quiz.quiz_type == "boolean":
            true_image = PhotoImage(file="images/true.png")
            false_image = PhotoImage(file="images/false.png")

            true_button = Button(image=true_image, highlightthickness=0, border=False, bg="blue",
                                 command=lambda: check("True"))
            true_button.grid(row=2, column=1)
            false_button = Button(image=false_image, highlightthickness=0, border=False, bg="blue",
                                  command=lambda: check("False"))
            false_button.grid(row=2, column=0)
        else:
            option_vars = [StringVar() for _ in range(4)]
            options = [Button(textvariable=option_vars[i],
                              font=("Cambria", 14, "normal"),
                              command=lambda x=i:
                              check(option_vars[x].get()))
                       for i in range(4)]
            options[0].grid(row=2, column=0, pady=5)
            options[1].grid(row=2, column=1, pady=5)
            options[2].grid(row=3, column=0, pady=5)
            options[3].grid(row=3, column=1, pady=5)

        get_next_question()

        window.resizable(False, False)
        window.eval(f'tk::PlaceWindow {window.winfo_pathname(window.winfo_id())} center')

        window.mainloop()
