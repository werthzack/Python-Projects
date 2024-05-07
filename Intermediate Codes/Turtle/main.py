import turtle
from random import *

new_turtle = turtle.Turtle()
new_turtle.speed(25)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "black", "grey", "brown"]


#----- Random Shape Generator------

#
# for num_sides in range(3, 35):
#     angle = 360/num_sides
#     new_turtle.color(choice(colors))
#     for side in range(num_sides):
#         new_turtle.left(angle)
#         new_turtle.forward(60)

#-------Random walk generator:
def is_out_of_screen():
    win_width = turtle.window_width()
    win_height = turtle.window_height()
    turtle_x = new_turtle.xcor()
    turtle_y = new_turtle.ycor()
    if turtle_x > win_width / 2 or turtle_x < -win_width / 2 or turtle_y > win_height / 2 or turtle_y < -win_height / 2:
        return True
    else:
        return False


def generate(sides=2, count=10):
    new_turtle.pensize(10)
    max_angle = 180 / sides
    angles = []
    cur = 0
    for a in range(sides):
        cur += max_angle
        if cur >= 180:
            break
        else:
            angles.append(cur)

    for i in range(count):
        angle = choice(angles)
        new_turtle.color(choice(colors))
        direction = choice([1, 2])
        if direction == 1:
            new_turtle.left(angle)
        else:
            new_turtle.right(angle)

        new_turtle.forward(50)
        # new_turtle.write(f"Step Count: {i}", align="center", font=("Arial", 16, "normal"))
        if is_out_of_screen() is True:
            print(i)
            break


def spiro_graph():
    turtle.colormode(255)
    angle = 0
    while angle <= 360:
        angle += 10
        new_turtle.color((randint(0,255)),randint(0,255),randint(0,255))
        new_turtle.setheading(angle)
        new_turtle.circle(100)

spiro_graph()

screen = turtle.Screen()
screen.exitonclick()
