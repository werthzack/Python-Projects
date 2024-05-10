import time
from turtle import Screen
from paddle import Paddle, AiPaddle
from ball import Ball
import random

screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("dark blue")
screen.tracer(0)

plr_Paddle = Paddle((-350, 0))
ai_Paddle = AiPaddle((350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(plr_Paddle.up, "Up")
screen.onkeypress(plr_Paddle.down, "Down")

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(.1)
    if plr_Paddle.distance(ball) < 20:
        pass

screen.exitonclick()
