import turtle
import time 
pen = turtle.Turtle() 

def oneside(l):
    pen.forward(l)  
    pen.left(90)
 
def cube(x, y, l, d, a):
    for i in range(4):
        oneside(142)

    pen.up()
    pen.goto(x + l, y)
    pen.down()
    pen.left(a)
    pen.forward(d)

    pen.up()
    pen.goto(l, l)
    pen.down()
    pen.forward(d)

    pen.up()
    pen.goto(x, l)
    pen.down()
    pen.forward(d)

    pen.right(a)
    pen.forward(l)
    pen.right(90)
    pen.forward(l)

cube(0, 0, 142, 123, 30)


time.sleep(5)