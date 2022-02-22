import imp
from tkinter import *

ball = {
            "dirx": 15,
            "diry": -15,
            "x" : 350,
            "y": 300,
            "w":10,
}

win = Tk()
cv = Canvas(win, width=600, height=400)
cv.pack()


def game_loop():
    draw_objects()
    move_ball()
    win.after(50, game_loop)

game_loop()
win.mainloop()