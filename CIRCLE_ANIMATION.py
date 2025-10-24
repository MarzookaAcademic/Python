import turtle
import time
import math  # <-- import math for cos and sin

screen = turtle.Screen()
screen.bgcolor("black")

circle = turtle.Turtle()
circle.shape("circle")
circle.color("cyan")
circle.shapesize(3)  # make circle bigger
circle.penup()
circle.speed(0)

radius = 200  # bigger orbit
angle = 0

while True:
    x = radius * math.cos(angle)  # use math.cos
    y = radius * math.sin(angle)  # use math.sin
    circle.goto(x, y)
    angle += 0.1
    time.sleep(0.02)
