from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.update_level(1)

    def update_level(self, level):
        self.clear()
        self.goto(-250, 260)
        self.write(f"Level: {level}", align="center", font=("Cambria", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Cambria", 20, "normal"))