from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.shape("circle")
        self.penup()
        self.shapesize(.5, .5)
        self.color("yellow")
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        x_cor = random.randrange(-280, 280, 20)
        y_cor = random.randrange(-280, 280, 20)
        self.goto(x_cor, y_cor)
