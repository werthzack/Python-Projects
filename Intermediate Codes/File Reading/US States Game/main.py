import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.bgpic(image)

data: pandas.DataFrame = pandas.read_csv("50_states.csv")
state_data = data.state
total_states = len(state_data)
correct_count = 0
states_found = []


def reveal_state(state: str):
    sel_state = data[state_data == state]
    new_t = turtle.Turtle()
    new_t.penup()
    new_t.shapesize(.2, .2)
    new_t.shape("circle")
    xcor = sel_state.x.iloc[0]
    ycor = sel_state.y.iloc[0]
    new_t.goto((xcor, ycor))
    new_t.write(state, align="center", font=("Cambria", 10, "normal"))


def reveal_all():
    states = data["state"].tolist()
    for state in states:
        print(state)
        if state in states_found:
            continue
        reveal_state(state)


while correct_count < total_states:
    guess = screen.textinput(title="Name the State", prompt="Name a state in America.\nType 'Reveal' to end the"
                                                            "game and reveal all the states")
    if guess == "" or guess is None:
        continue
    guess = guess.title()
    if guess == "Reveal":
        reveal_all()
        break
    elif guess in states_found:
        continue

    if data[state_data == guess].empty is False:
        states_found.append(guess)
        reveal_state(guess)

screen.mainloop()
