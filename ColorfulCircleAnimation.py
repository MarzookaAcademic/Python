import turtle
import math
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.width(3)

hue = 0.0

for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(color)
    t.circle(100)
    t.right(10)
    hue += 0.005

turtle.done()
