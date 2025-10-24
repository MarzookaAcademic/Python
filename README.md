# Python
import turtle
import time

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
    x = radius * turtle.cos(angle)
    y = radius * turtle.sin(angle)
    circle.goto(x, y)
    angle += 0.1
    time.sleep(0.02)
