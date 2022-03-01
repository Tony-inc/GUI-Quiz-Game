from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.continue_quiz = False
        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 16, "italic"))
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        self.question = self.canvas.create_text(150, 125,
                                                width=280,
                                                text="Question Here",
                                                font=("Arial", 20, "italic"))

        yes_image = PhotoImage(file="images/true.png")
        no_image = PhotoImage(file="images/false.png")
        color = "green"
        self.button_yes = Button(image=yes_image, highlightthickness=0,
                                 bg=THEME_COLOR, highlightbackground=THEME_COLOR,
                                 command=self.true_button)
        self.button_yes.grid(row=2, column=0)
        self.button_no = Button(image=no_image, highlightthickness=0,
                                bg=THEME_COLOR, highlightbackground=THEME_COLOR,
                                command=self.false_button)
        self.button_no.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def check_the_question(self):
        correct_answer = self.quiz.current_question.answer
        if self.user_answer == correct_answer:
            self.color_bg("green")
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
        else:
            self.color_bg("red")

        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            self.label.config(text="")
            self.canvas.itemconfig(self.question, text=f"Your final score: {self.score}")
            self.button_yes.destroy()
            self.button_no.destroy()
            self.continue_button = Button(text="START AGAIN", highlightthickness=0, bg=THEME_COLOR, fg=THEME_COLOR,
                                          width=30, command=self.click)
            self.continue_button.grid(column=0, row=2, columnspan=2)
            # self.button_yes.config(command=self.remove_command)

    # def remove_command(self):
    #     pass

    def color_bg(self, color):
        self.window.config(background=color)
        self.label.config(bg=color)
        self.button_yes.config(bg=color, highlightbackground=color)
        self.button_no.config(bg=color, highlightbackground=color)
        self.window.after(700, self.restore_bg)

    def restore_bg(self):
        self.window.config(background=THEME_COLOR)
        self.label.config(bg=THEME_COLOR)
        self.button_yes.config(bg=THEME_COLOR, highlightbackground=THEME_COLOR)
        self.button_no.config(bg=THEME_COLOR, highlightbackground=THEME_COLOR)

    def false_button(self):
        self.user_answer = "False"
        self.check_the_question()

    def true_button(self):
        self.user_answer = "True"
        self.check_the_question()

    def click(self):
        self.continue_quiz = True
        self.window.destroy()








