import turtle
import random
stamp = turtle.Turtle()
stamp.shape('turtle')
stamp.penup
turtle.colormode(255)
paces = 20
for i in range(50):
  random_red = random.randint(0,225)
  random_green = random.randint(0,225)
  random_blue = random.randint(0,225)
  stamp.color(random_red, random_green, random_blue)
  stamp.stamp()
  paces += 3
  stamp.forward(paces)
  stamp.right(25)