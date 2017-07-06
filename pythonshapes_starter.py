from turtle import *
import math
import time

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below

delay (50)


showturtle()
begin_fill()
pendown()
pensize (5)
pencolor("red")
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

color("violet")
end_fill()
penup()

time.sleep(2)

reset()

time.sleep(1)
begin_fill()
pendown()
pensize (5)
pencolor("green")
for i in range(3):
    forward(100)
    left(120)

color("yellow")
end_fill()




# Close window on click.
exitonclick()
