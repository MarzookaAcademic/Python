import turtle
import random

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(200):
    t.color(random.choice(colors))
    t.circle(i)
    t.left(60)
    t.circle(i * 0.8)
    t.left(60)

turtle.done()
