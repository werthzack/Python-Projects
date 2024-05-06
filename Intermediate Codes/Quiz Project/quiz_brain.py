import random


class QuizManager:
    def __init__(self, data: list):
        self.question_number = 0
        new_data = []
        while len(data) >= 1:
            question = random.choice(data)
            data.remove(question)
            new_data.append(question)

        self.question_data = new_data

    def next_question(self):
        question = self.question_data[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False) ")
        question_answer = question.answer

        if answer.title() != "True" and answer.title() != "False":
            print("Invalid Answer, Retry")
            self.next_question()

        if answer.title() == question_answer:
            self.question_number += 1
            if self.question_number >= len(self.question_data):
                print("Correct!")
                print("All Questions answered! You win")
            else:
                print("Correct! Next Question")
                self.next_question()
        else:
            print("Wrong! Game Over!")
            return

    def start_quiz(self):
        print("Welcome To the Quiz, Pls answer all questions with either TRUE or False")
        self.next_question()
