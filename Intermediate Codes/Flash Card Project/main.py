from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"

try:
    words_data = read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_data = read_csv("./data/french_words.csv")
word_dict = words_data.to_dict(orient="records")

timer: str = ""
cur_word: dict = {}


def next_card():
    global cur_word, timer
    if timer != "":
        new_window.after_cancel(timer)
    cur_word = choice(word_dict)
    canvas.itemconfig(board, image=card_image)
    canvas.itemconfig(title, text="French", fill=BLACK)
    canvas.itemconfig(word, text=cur_word["French"], fill=BLACK)
    timer = new_window.after(3000, reveal)


def reveal():
    canvas.itemconfig(title, text="English", fill=WHITE)
    canvas.itemconfig(word, text=cur_word["English"], fill=WHITE)
    canvas.itemconfig(board, image=reveal_image)


def learnt_card():
    word_dict.remove(cur_word)
    next_card()


new_window = Tk()
new_window.title("Flash Card Project")
new_window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

card_image = PhotoImage(file="./images/card_front.png")
reveal_image = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
board = canvas.create_image(400, 260, image=card_image)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=learnt_card)
right_button.grid(column=1, row=1)

next_card()

new_window.mainloop()
learn_data = DataFrame(word_dict)
learn_data.to_csv("./data/words_to_learn.csv", index=False)
