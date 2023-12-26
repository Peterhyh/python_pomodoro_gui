from tkinter import *

window = Tk()
window.title("Pomodoro")

background = PhotoImage(file="background.png")
canvas = Canvas(width=200, height=224)
canvas.create_image(100, 112, image=background)
canvas.pack()

window.mainloop()
