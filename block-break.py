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

def draw_objects():
    cv.delete('all')
    cv.create_oval(
        ball["x"] - ball["w"], ball["y"] - ball["w"],
        ball["x"] + ball["w"], ball["y"] + ball["w"],
        fill="green")

def move_ball():
    # 仮の変数に移動後の値を記録
    bx = ball["x"] + ball["dirx"]
    by = ball["y"] + ball["diry"]

    # 上下の壁に当たった？
    if bx < 0 or bx > 600: ball["dirx"] *= -1
    if by < 0 or by > 400: ball["diry"] *= -1

    # 移動内容を反映
    if 0 <= bx <= 600: ball["x"] = bx
    if 0 <= by <= 400: ball["y"] = by

def game_loop():
    draw_objects()
    move_ball()
    win.after(50, game_loop)

game_loop()
win.mainloop()