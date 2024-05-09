import turtle
import time


class Snake:
    def __init__(self):
        self.length = 3
        self.segments = []
        self.head = None
        self.create()

    def create(self, xcor=0):
        for i in range(self.length):
            new_square = turtle.Turtle("square")
            new_square.color("white")
            new_square.penup()
            if self.head is None:
                self.head = new_square
                new_square.color("black")
            new_square.goto(xcor, 0)
            xcor -= 20
            self.segments.append(new_square)

    def move(self):
        for i in range(len(self.segments), 0, -1):
            cur_seg = self.segments[i - 1]
            if self.head != cur_seg:
                prev_seg = self.segments[i - 2]
                cur_seg.goto(prev_seg.xcor(), prev_seg.ycor())
            else:
                self.head.forward(20)

    def left(self):
        heading = self.head.heading()
        if heading == 180.0 or heading == 0.0:
            return
        else:
            self.segments[0].setheading(180)

    def right(self):
        heading = self.head.heading()
        if heading == 180.0 or heading == 0.0:
            return
        else:
            self.segments[0].setheading(0)

    def up(self):
        heading = self.head.heading()
        if heading == 90.0 or heading == 270.0:
            return
        else:
            self.segments[0].setheading(90)

    def down(self):
        heading = self.head.heading()
        if heading == 90.0 or heading == 270.0:
            return
        else:
            self.segments[0].setheading(270)

