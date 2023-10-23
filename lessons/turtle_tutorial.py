"""The Turtle Tutorial and Into to Project."""
__author__ = "730467698"

from turtle import Turtle, colormode, done
colormode(255)

"""Presenting 'leo'."""
leo: Turtle = Turtle()

leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-130, -130)
leo.down()

leo.color(226, 146, 249)
leo.begin_fill()
l: int = 0
while (l < 3):
    leo.forward(300)
    leo.left(120)
    l = l + 1
leo.end_fill()

"""Presenting 'bob'."""
bob: Turtle = Turtle()

bob.hideturtle()
bob.speed(150)

bob.penup()
bob.goto(-130, -130)
bob.down()

bob.color(0, 0, 0)
b: int = 0
while (b < 3):
    bob.forward(300)
    bob.left(120)
    b = b + 1

side_length: int = 300
s: int = 0
while (s < 100):
    bob.forward(side_length)
    bob.left(120.5)
    side_length = side_length * 0.97
    s = s + 1

done()
