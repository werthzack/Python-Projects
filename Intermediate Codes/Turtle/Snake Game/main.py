import time
import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = t.Screen()
screen.bgcolor("green")
screen.setup(600, 600)
screen.tracer(0)

new_snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")

game_over = False


while game_over is False:
    new_snake.move()
    screen.update()
    time.sleep(.1)

    if new_snake.head.distance(food) < 15:
        food.new_location()
        new_snake.extend()
        scoreboard.add_point()

    xcor = new_snake.head.xcor()
    ycor = new_snake.head.ycor()

    if xcor >= 280 or xcor <= -280 or ycor >= 280 or ycor <= -280:
        scoreboard.game_over()
        game_over = True

    snake_body = new_snake.segments[1:]
    for segment in snake_body:
        if new_snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
