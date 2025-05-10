import turtle as t
from turtle import Screen

tim = t.Turtle()

# Challenge 1 - Draw a Dashed Line
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()