import html


class QuizBrain:

    def __init__(self, q_list, q_type):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.quiz_type = q_type

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return html.unescape(f"Q{self.question_number}:{self.current_question.text}")

    def get_options(self):
        return self.current_question.wrong_answers, self.current_question.answer

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
