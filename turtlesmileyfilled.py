import turtle
import time
my_pen = turtle.Turtle()      

def eye(rad):
    my_pen.down()
    my_pen.circle(rad)
    my_pen.up()

my_pen.fillcolor('yellow')
my_pen.begin_fill()
my_pen.circle(100)
my_pen.end_fill()
my_pen.up()

my_pen.goto(-40, 120)
my_pen.fillcolor('blue')
my_pen.down()
my_pen.begin_fill()
my_pen.circle(10)
my_pen.end_fill()
my_pen.up()

my_pen.goto(40, 120)
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
time.sleep(30)
#my_pen.down()
#oord = 10, 50, 240, 210
#my_pen.arc()