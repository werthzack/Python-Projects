from question_model import Question
from data import question_data
from quiz_brain import QuizManager

question_bank = []

for data in question_data:
    new_question = Question(data["text"], data["answer"])
    question_bank.append(new_question)

new_manager = QuizManager(question_bank)
new_manager.start_quiz()
