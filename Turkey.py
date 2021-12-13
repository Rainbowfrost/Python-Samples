import turtle
import time 
pen = turtle.Turtle() 
def body(d):
    pen.up()
    pen.goto(0, -50)
    pen.fillcolor('brown')
    pen.begin_fill()
    pen.down()
    pen.circle(d)
    pen.end_fill()
    pen.up()

def legs(x, y, g, t):
    pen.setheading(270)
    pen.goto(x, y) 
    pen.down()
    pen.forward(30)
    pen.up()
    pen.right(45)
    for i in range(3):
        pen.goto(g, t)
        pen.down()
        pen.forward(10)
        pen.up()
        pen.left(45)
    pen.up()

def head(d):
    pen.goto(0, 150)
    pen.fillcolor('brown')
    pen.begin_fill()
    pen.down()
    pen.circle(d/3)
    pen.end_fill()
    pen.up()
pen.hideturtle()

#for i in range(3):






body(100)
legs(-10, -150, -10, -120)
legs(10, -150, 10, -120)
head(100)


time.sleep(5)