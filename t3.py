from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
numsides = input("How many sides?")

t.goto(0,0)
pendown()
for shape in range(numsides):
        forward(100)
        left(360/numsides)





# Close window on click.
exitonclick()
