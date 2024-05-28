from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Cambria"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# NON-CONSTANTS
timer: str = ""
reps = 0
session = 0
on_timer = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, session, on_timer
    if timer != "":
        window.after_cancel(timer)
    change_color("#ffffff")
    title_text.config(text="Pomodoro Timer", foreground=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = session = 0
    on_timer = False


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps, session, on_timer
    if on_timer:
        return
    reps += 1
    on_timer = True
    if reps % 8 == 0:
        title_text.config(text="Long Break", foreground=YELLOW)
        change_color(RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_text.config(text="Short Break", foreground=GREEN)
        change_color(PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        session += 1
        title_text.config(text=f"Work Session {session}", foreground=RED)
        change_color(YELLOW)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def change_color(color):
    title_text.config(background=color)
    canvas.config(background=color)
    window.config(background=color)


def end_timer():
    global timer, on_timer
    if timer != "":
        window.after_cancel(timer)
        on_timer = False
        start_timer()


def count_down(count):
    global timer, on_timer
    text = "{min}:{sec}".format(min=int(count / 60), sec=(count % 60) if (count % 60) >= 10 else f"0{(count % 60)}")
    canvas.itemconfig(timer_text, text=text)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        on_timer = False
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=250, highlightthickness=0)
canvas.create_image(100, 125, image=image)
timer_text = canvas.create_text(100, 140, text="00:00", font=("Cambria", 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=("Cambria", 15, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=("Cambria", 15, "bold"), command=reset_timer)
reset_button.grid(column=2, row=2)

complete_button = Button(text="Complete", font=("Cambria", 10, "bold"), command=end_timer)
complete_button.grid(column=1, row=2)

title_text = Label(text="Pomodoro Session", font=("Cambria", 15, "bold"), foreground=GREEN)
title_text.grid(column=1, row=0)

window.mainloop()
