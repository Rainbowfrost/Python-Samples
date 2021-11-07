import turtle
import time
my_pen = turtle.Turtle() 



def drawRays(t, length, radius, numberofrays):
    for i in range(numberofrays):
        my_pen.penup()
        my_pen.forward(radius)
        my_pen.pendown()
        if i%2 == 0:
            l = length
        else:
            l = length * 0.75
        my_pen.forward(l) 
        my_pen.penup()
        my_pen.backward(l + radius)
        my_pen.left(360/numberofrays)



my_pen.fillcolor('yellow')
my_pen.begin_fill()
my_pen.circle(100)
my_pen.end_fill()
my_pen.up()

my_pen.penup()
my_pen.goto(0, 100)
my_pen.pendown()
drawRays(my_pen, 100, 100, 8)
my_pen.right(45)

def eye(rad):
    my_pen.down()
    my_pen.circle(rad)
    my_pen.up()
    my_pen.goto(-60, 120)

my_pen.goto(-60, 120)
my_pen.fillcolor('blue')
my_pen.down()
my_pen.begin_fill()
my_pen.circle(10)
my_pen.end_fill()
my_pen.up()

my_pen.goto(50, 120)
my_pen.fillcolor('blue')
my_pen.down()
my_pen.begin_fill()
my_pen.circle(10)
my_pen.end_fill()
my_pen.up()

my_pen.goto(-40, 70)
my_pen.down()
my_pen.right(90)
my_pen.circle(40, 180)
my_pen.up()


'''my_pen.goto(95, 50)
my_pen.pendown()
#my_pen.right(45)
my_pen.forward(105)
my_pen.up

my_pen.goto(100, 100)
my_pen.pendown()
my_pen.forward(105)
my_pen.up()

my_pen.goto(0, 0)
my_pen.pendown()
my_pen.right(90)
my_pen.forward(105)
my_pen.up()

my_pen.goto(-100, 100)
my_pen.pendown()
my_pen.right(90)
my_pen.forward(105)
my_pen.up()

my_pen.goto(0, 200)
my_pen.pendown()
my_pen.right(90)
my_pen.forward(105)'''


time.sleep(5)


