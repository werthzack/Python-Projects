import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)

rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


def race(turtles=None, chosen_turtle=None):
    ycor = 90
    if turtles is None:
        turtles = []

        for i in range(len(rainbow_colors)):
            color = rainbow_colors[i]
            new_turtle = t.Turtle()
            new_turtle.color(color)
            new_turtle.penup()
            new_turtle.shape("turtle")
            new_turtle.goto(-230, ycor)
            ycor -= 30
            turtles.append({
                "turtle": new_turtle,
                "turned": False
            })
    else:
        for i in range(len(turtles)):
            cur_turtle = turtles[i]["turtle"]
            turtles[i]["turned"] = False
            cur_turtle.goto(-230, ycor)
            ycor -= 30

    if chosen_turtle is None:
        chosen_turtle = screen.textinput(title="Select Turtle", prompt="Select the turtle you vote for the race")
        while chosen_turtle not in rainbow_colors:
            chosen_turtle = screen.textinput(title="Invalid Input", prompt="Select the color on a rainbow")

    winner = None
    while winner is None:
        for i in range(len(turtles)):
            turned = turtles[i]["turned"]
            cur_turtle = turtles[i]["turtle"]
            random_distance = random.randint(1, 10)
            cur_turtle.forward(random_distance)
            if cur_turtle.xcor() > 230:
                turtles[i]["turned"] = True
                cur_turtle.setheading(180)

            if turned is True and cur_turtle.xcor() < -230:
                winner = rainbow_colors[i]

    print(f"{winner} turtle won the race!")
    if len(turtles) > 3:
        last_pos = -230
        last_color = ""
        last_index = None
        for i in range(len(turtles)):
            cur_turtle = turtles[i]["turtle"]
            if cur_turtle.xcor() > last_pos:
                last_color = rainbow_colors[i]
                last_pos = cur_turtle.xcor()
                last_index = i
            cur_turtle.home()
            turtles[i]["turned"] = False

        tar_turtle = turtles[last_index]["turtle"]
        turtles.remove(turtles[last_index])
        tar_turtle.hideturtle()
        rainbow_colors.remove(rainbow_colors[last_index])

        if last_color == chosen_turtle:
            print(f"Your turtle has been knocked out from the championship")
            return
        race(turtles,chosen_turtle)
    else:
        print(f"{winner} turtle won the Championship! \n\nYou chose {chosen_turtle} turtle!")
        if winner == chosen_turtle:
            print("Your turtle won the race!!")
        else:
            print("Awwn, too bad! Your turtle didn't win the race")


race()

screen.exitonclick()
