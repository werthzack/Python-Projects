from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -250)

    def up(self):
        y_cor = self.ycor() + 50
        self.goto(0, y_cor)
