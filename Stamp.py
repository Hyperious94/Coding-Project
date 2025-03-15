# David Wheeler
# Passport Stamp
# COP 2500
# 04/06/2024

import turtle

def travel (x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.shape("turtle")
turtle.speed(10)
turtle.pensize(2)

# Draw the large square
travel (-150,-150)
turtle.color("#FFDF00")
turtle.begin_fill()

for count in range(4):
    turtle.forward(300)
    turtle.left(90)

turtle.end_fill()

#SW Corner
turtle.color("#0834ef")
turtle.begin_fill()
for count in range(4):
    turtle.right(90)
    turtle.forward(25)
turtle.end_fill()

#SE Corner
travel(150,-150)
turtle.color("#0834ef")
turtle.begin_fill()
for count in range(4):
    turtle.forward(25)
    turtle.right(90)
turtle.end_fill()

#NE Corner
travel(150,150)
turtle.color("#0834ef")
turtle.begin_fill()
for count in range(4):
    turtle.forward(25)
    turtle.left(90)
turtle.end_fill()

#NW Corner
travel(-150,150)
turtle.color("#0834ef")
turtle.begin_fill()
for count in range(4):
    turtle.left(90)
    turtle.forward(25)
turtle.end_fill()

# Draw the middle stamp(circle)
travel (0,-120)
turtle.color("#f54842")
turtle.begin_fill()
turtle.circle(120)
turtle.end_fill()

# Middle of circle
turtle.color("#FFDF00")
travel(-120,-20)
turtle.begin_fill()

turtle.forward(240)
turtle.left(90)
turtle.forward(40)
turtle.left(90)
turtle.forward(240)
turtle.left(90)
turtle.forward(40)

turtle.end_fill()

# Write "Barcelona" inside the rectangle
turtle.color("black")
travel(0, -10)  # Adjust position to center the text
turtle.write("Barcelona", align ="center", font=("Times New Roman", 20, "bold"))

# End turtle drawing
turtle.hideturtle()
turtle.done()



    



    
    
