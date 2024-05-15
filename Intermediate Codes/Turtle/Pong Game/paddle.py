from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.move_speed = 20
        self.penup()
        self.shapesize(3, 0.5)
        self.goto(position)

    def up(self):
        if self.ycor() >= 260:
            return
        self.goto(self.xcor(), self.ycor() + self.move_speed)

    def down(self):
        if self.ycor() <= -260:
            return
        self.goto(self.xcor(), self.ycor() - self.move_speed)


class AiPaddle(Paddle):
    def __init__(self, position):
        super().__init__(position)

    def track(self, ball):
        if ball.ycor() > self.ycor() + 30:
            self.up()
        elif ball.ycor() < self.ycor() - 30:
            self.down()
