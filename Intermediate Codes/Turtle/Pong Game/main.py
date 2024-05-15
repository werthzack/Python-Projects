import time
from turtle import Screen
from paddle import Paddle, AiPaddle
from ball import Ball
from scoreboard import ScoreBoard

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

plr_score = 0
ai_score = 0

new_score = ScoreBoard()
new_score.score(plr_score, ai_score)

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(.1)

    if 0 < ball.xcor() < 360:
        ai_Paddle.track(ball)

    if (plr_Paddle.distance(ball) < 50 and ball.xcor() < -340) or (ai_Paddle.distance(ball) < 50 and ball.xcor() > 340):
        ball.x_move *= -1.1
        ball.move()

    if ball.xcor() > 400:
        plr_score += 1
        new_score.score(plr_score, ai_score)
        ball.reset_position()
        ai_Paddle.move_speed += 1
    elif ball.xcor() < -400:
        ai_score += 1
        new_score.score(plr_score, ai_score)
        ball.reset_position()
        plr_Paddle.move_speed += 1

    if plr_score > 10:
        new_score.win("Player")
        game_on = False
    elif ai_score > 10:
        new_score.win("AI")
        game_on = False

screen.exitonclick()
