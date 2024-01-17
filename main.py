from tkinter import *
import time
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0


# Start Timer logic ---------------------------------------------------------
def start_timer():
    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        count_down(long_break_seconds)
        title.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title.config(text="Short Break", fg=PINK)
    else:
        count_down(work_seconds)
        title.config(text="Work", fg=GREEN)


# Count down logic ---------------------------------------------------------
def count_down(count):

    minutes = math.floor(count/60)
    seconds = count % 60

    if minutes == 0:
        minutes = "00"
    elif minutes < 10 and minutes > 0:
        minutes = "0" + f"{minutes}"
    if seconds == 0 and seconds > 0:
        seconds = "00"
    elif seconds < 10:
        seconds = "0" + f"{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


# UI Codes ---------------------------------------------------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

background_img = PhotoImage(file="background.png")

title = Label(text="Timer", bg=YELLOW, font=("Ariel", 50), fg=GREEN)
title.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=background_img)


timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))


canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

window.mainloop()
