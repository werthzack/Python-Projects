import turtle
import time


class Snake:
    def __init__(self):
        self.length = 3
        self.segments = []
        self.head = None
        self.create()

    def create(self):
        position = (0, 0)
        for i in range(self.length):
            if self.head is None:
                self.add_segment(position)
                self.head = self.segments[0]
            else:
                self.add_segment(self.segments[-1].position())

        self.head.color("black")

    def add_segment(self, position):
        new_square = turtle.Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.head = None
        self.create()

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
            self.head.setheading(180)

    def right(self):
        heading = self.head.heading()
        if heading == 180.0 or heading == 0.0:
            return
        else:
            self.head.setheading(0)

    def up(self):
        heading = self.head.heading()
        if heading == 90.0 or heading == 270.0:
            return
        else:
            self.head.setheading(90)

    def down(self):
        heading = self.head.heading()
        if heading == 90.0 or heading == 270.0:
            return
        else:
            self.head.setheading(270)
