from tkinter import *
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


def count_down(count):
    window.after(1000, count_down, count - 1)


background_img = PhotoImage(file="background.png")

title = Label(text="Timer", bg=YELLOW, font=("Ariel", 50), fg=GREEN)
title.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=background_img)
canvas.create_text(100, 130, text="00:00", fill="white",
                   font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

window.mainloop()
