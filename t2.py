from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below
for sides in range(4):
    t.forward(100)
    t.left(90)



# Close window on click.
exitonclick()
