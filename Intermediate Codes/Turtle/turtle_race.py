import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def race():
    turtles = []
    ycor = 90
    for i in range(len(rainbow_colors)):
        color = rainbow_colors[i]
        new_turtle = turtle.Turtle()
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.shape("turtle")
        new_turtle.goto(-230, ycor)
        ycor -= 30
        turtles.append(new_turtle)

    chosen_turtle = screen.textinput(title="Select Turtle", prompt="Select the turtle you vote for the race")
    while not chosen_turtle in rainbow_colors:
        chosen_turtle = screen.textinput(title="Invalid Input", prompt="Select the color on a rainbow")

    winner = None

    while winner is None:
        for each in turtles:
            random_distance = random.randint(1, 10)
            each.forward(random_distance)
            if each.xcor() > 230:
                winner = rainbow_colors[turtles.index(each)]

    print(f"{winner} turtle won the race! \nYou chose {chosen_turtle} turtle! \n")
    if winner == chosen_turtle:
        print("Your turtle won the race!!")
    else:
        print("Awwn, too bad! Your turtle didn't win the race")


race()

screen.exitonclick()
