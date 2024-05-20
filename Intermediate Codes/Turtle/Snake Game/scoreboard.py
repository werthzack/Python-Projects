from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.highscore = 0
        self.get_highscore()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def get_highscore(self):
        with open("highscore.txt") as file:
            contents = file.read()
            score = int(contents.strip("Highscore = "))
            self.highscore = score

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Cambria", 24, "normal"))

    def add_point(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as file:
                file.write(f"Highscore = {self.highscore}")
        self.score = 0
        self.update_score()
