from turtle import *
import math

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



reset()

begin_fill()
pendown()
pencolor("green")
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)

color("yellow")
end_fill()




# Close window on click.
exitonclick()
