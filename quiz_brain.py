import html

class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = q_bank
        self.q_text = ""
        self.a_text = ""

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.a_text = current_question.answer
        self.question_number += 1
        self.q_text = html.unescape(current_question.text)
        return f"Q.{self.question_number}: {self.q_text}"

    def check_answer(self, user_answer):
        correct_answer = self.a_text
        if user_answer == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
