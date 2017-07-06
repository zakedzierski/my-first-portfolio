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
input_var  = int(input("Type a number: "))

t.goto(0,0)
pendown()
for shape in range(input_var):
        forward(100)
        left(360/input_var)





# Close window on click.
exitonclick()
