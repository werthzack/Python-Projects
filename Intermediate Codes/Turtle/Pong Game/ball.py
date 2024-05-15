from turtle import Turtle
import time
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = -10
        self.y_move = -10

    def check_boundary(self):
        ycor = self.ycor()

        if ycor > 280 or ycor < -280:
            self.y_move *= -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.check_boundary()

    def reset_position(self):
        self.goto(0, 0)
        self.x_move = 10
        time.sleep(1)
