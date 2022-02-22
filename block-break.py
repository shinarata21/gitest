import imp
from tkinter import *

ball = {
            "dirx": 15,
            "diry": -15,
            "x" : 350,
            "y": 300,
            "w":10,
}

blocks = []

for iy in range(0 ,8):
    for ix in range(0,8):
        color = "red"
        if (iy + ix) % 2 == 1: color = "blue"
        x1 = 4 + ix * block_size["x"]
        x2 = x1 + block_size["x"]
        y1 = 4 + iy * block_size["y"]
        y2 = y1 + block_size["y"]
        blocks.append([x1,y1,x2,y2,color])

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