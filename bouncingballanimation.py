import tkinter as tk
import random

root = tk.Tk()
root.title("Bouncing Ball Animation")

canvas = tk.Canvas(root, width=400, height=300, bg="black")
canvas.pack()

ball = canvas.create_oval(10, 10, 40, 40, fill="cyan")
dx, dy = 3, 2

def animate():
    global dx, dy
    canvas.move(ball, dx, dy)
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 <= 0 or x2 >= 400:
        dx = -dx
    if y1 <= 0 or y2 >= 300:
        dy = -dy
    root.after(10, animate)

animate()
root.mainloop()
