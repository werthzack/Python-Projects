from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(0, 360))

    def check_boundary(self):
        xcor = self.xcor()
        ycor = self.ycor()

        if ycor > 280 or ycor < -280:
            self.setheading(-self.heading())

    def move(self):
        self.forward(10)
        self.check_boundary()
