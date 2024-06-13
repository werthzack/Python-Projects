class Question:
    def __init__(self, q_text, q_answer, q_category, wrong_answer=None):
        self.text = q_text
        self.answer = q_answer
        self.category = q_category
        self.wrong_answers = wrong_answer
