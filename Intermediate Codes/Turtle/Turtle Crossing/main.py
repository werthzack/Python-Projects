from turtle import Screen
from player import Player
from road import Road
from scoreboard import ScoreBoard
import time
import random

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.bgcolor("white")
screen.tracer(0)

level = 1
crashed = False
car_chance = 1
blank_chance = 3

new_Player = Player()
new_road = Road()
score = ScoreBoard()

screen.listen()
screen.onkeypress(new_Player.up, "Up")


def set_pool():
    pool = []
    for i in range(car_chance):
        pool.append("Car")
    for i in range(blank_chance):
        pool.append("Blank")
    return pool


choice_pool = set_pool()

while not crashed:
    time.sleep(.1)
    if random.choice(choice_pool) == "Car":
        new_road.spawn_car()

    new_road.move_cars()

    for car in new_road.cars:
        if new_Player.distance(car) < 25:
            score.game_over()
            crashed = True

    if new_Player.ycor() >= 300:
        new_Player.goto(0, -250)
        if car_chance < 7:
            car_chance += 1
        choice_pool = set_pool()
        new_road.move_speed += 2
        level += 1
        score.update_level(level)

    screen.update()

screen.exitonclick()
