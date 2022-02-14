import turtle
import time 

n = int(input('How many circles do you want?\n'))
d = int(input('How far apart do you want the circles?\n'))
l = int(input('What is the diameter of the first circle?\n'))
i = 0

pen = turtle.Turtle()

def circle(l,x,y):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.circle(l)
    pen.end_fill()
    pen.up()

y = 0
while i < n:
    circle(l, 0, y)
    y = y - d
    l = l + d
    i = i + 1
