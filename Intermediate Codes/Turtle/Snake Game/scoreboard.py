from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Cambria", 24, "normal"))
        self.hideturtle()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Cambria", 24, "normal"))