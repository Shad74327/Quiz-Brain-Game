from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="black", bg=THEME_COLOR, highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.config(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", fill="black",
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_img = PhotoImage(file="images/true.png")
        self.check_button = Button(image=check_img, highlightthickness=0, command=self.true_pressed)
        self.check_button.grid(row=2, column=0)

        cross_img = PhotoImage(file="images/false.png")
        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
