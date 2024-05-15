from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

    def score(self, l_score=0, r_score=0):
        self.clear()
        self.goto(-100, 250)
        self.write(l_score, align="center", font=("Cambria", 30, "normal"))
        self.goto(0, 250)
        self.write(" : ", align="center", font=("Cambria", 30, "normal"))
        self.goto(100, 250)
        self.write(r_score, align="center", font=("Cambria", 30, "normal"))

    def win(self, winner):
        self.goto(0, 0)
        self.write(f"{winner} won the game", align="center", font=("Cambria", 30, "normal"))