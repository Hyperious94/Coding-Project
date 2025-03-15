# David Wheeler
# Passport
# COP 2500
# 04/06/2024

import turtle


def travel (x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def David_Wheeler_Stamp(x,y):
    turtle.shape("turtle")
    turtle.speed(10)
    turtle.pensize(2)

    # Draw the large square
    travel (x-75,x-75)
    turtle.color("#FFDF00")
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(150)
        turtle.left(90)

    turtle.end_fill()

    #SW Corner
    turtle.color("#0834ef")
    turtle.begin_fill()
    for count in range(4):
        turtle.right(90)
        turtle.forward(12.5)
    turtle.end_fill()

    #SE Corner
    travel(x+75,x-75)
    turtle.color("#0834ef")
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(12.5)
        turtle.right(90)
    turtle.end_fill()

    #NE Corner
    travel(x+75,x+75)
    turtle.color("#0834ef")
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(12.5)
        turtle.left(90)
    turtle.end_fill()

    #NW Corner
    travel(x-75,x+75)
    turtle.color("#0834ef")
    turtle.begin_fill()
    for count in range(4):
        turtle.left(90)
        turtle.forward(12.5)
    turtle.end_fill()

    # Draw the middle stamp(circle)
    travel (x+0,x-60)
    turtle.color("#f54842")
    turtle.begin_fill()
    turtle.circle(60)
    turtle.end_fill()

    # Middle of circle
    turtle.color("#FFDF00")
    travel(x-60,x-10)
    turtle.begin_fill()

    turtle.forward(120)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(20)

    turtle.end_fill()

    # Write "Barcelona" inside the rectangle
    turtle.color("black")
    travel(x+0, x-10)  # Adjust position to center the text
    turtle.write("Barcelona", align ="center", font=("Times New Roman", 20, "bold"))

    # End turtle drawing
    turtle.hideturtle()
    turtle.setheading(0)
    #turtle.done()


# Stamp 2

import turtle

#create travel function so i dont have to type pen up pen down a million times
def travel(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


#define stamp
def Nathan_Forrer_Stamp(x,y):
    turtle.speed(0)
    #set variables to adjust design size
    margin=10
    size=150-2*margin
    designRad=size/2-2*margin
    gearOR=designRad-margin*.5
    gearIR=gearOR-margin*.5
    teeth=10
    detailGap=3*margin
    color1="#97a9f0"
    color2="#e8f1ff"

    turtle.speed(0)
    #set stamp centered at x,y
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(x-size/2-margin,y-size/2)
    turtle.pendown()
    
    #draw stamp outline
    turtle.fillcolor(color2)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(size+2*margin)
        turtle.right(90)
        turtle.fd(margin)
        turtle.right(90)
        turtle.fd(margin)
        turtle.right(90)
    turtle.end_fill()

    #draw outline details
    travel(x-size/2+margin,y-size/2-margin)
    turtle.setheading(0)
    for i in range(4):
        turtle.fd(size-2*margin)
        turtle.penup()
        turtle.fd(2*margin)
        turtle.left(90)
        turtle.fd(2*margin)
        turtle.pendown()

    turtle.fillcolor(color1)
    turtle.begin_fill()
    #draw gear because i am mechanical engineering
    travel(x+gearIR,y)
    turtle.setheading(90)
    #gear loop (draws segment of gear "teeth" number of times)
    for i in range (teeth):
        turtle.circle(gearIR,360/(2*teeth))
        turtle.right(90)
        turtle.fd(gearOR-gearIR)
        turtle.left(90)
        turtle.circle(gearOR,360/(2*teeth))
        turtle.left(90)
        turtle.fd(gearOR-gearIR)
        turtle.right(90)
    turtle.end_fill()
    #gear hole
    turtle.fillcolor(color2)
    turtle.begin_fill()
    travel(x+margin,y)
    turtle.setheading(90)
    turtle.circle(margin)
    turtle.end_fill()
    
    #draw inner details becasue i like line art
    travel(x+detailGap,y-size/2+margin)
    turtle.setheading(0)
    for i in range(4):
        turtle.fd(size/2-detailGap-margin)
        turtle.left(90)
        turtle.fd(size/2-detailGap-margin)
        turtle.penup()
        turtle.fd(size-2*(size/2-detailGap-margin)-2*margin)
        turtle.pendown()
    
    
# Stamp 3

my_screen = turtle.getscreen()
my_turtle = turtle.Turtle()
my_turtle.speed(1000)

#Makes stamp squiggle pattern
def Emma_Lundquist_Stamp(x,y):
    my_turtle.circle(5,180)
    my_turtle.circle(-5,180)
    my_turtle.circle(5,180)
    my_turtle.circle(-5,180)

#Draws and fills the stamp    
def stamp_fill(x,y):
    my_turtle.penup()
    my_turtle.goto(x,y)
    my_turtle.pendown()
    my_turtle.color("#a3905b")
    my_turtle.begin_fill()
    for count in range(4):
        squiggle()
        squiggle()
        squiggle()
        squiggle()
        squiggle()
        my_turtle.right(90)
    my_turtle.end_fill()

#Outlines the stamp in black
def stamp_outline():
    my_turtle.color("#000000")
    for count in range(4):
        squiggle()
        squiggle()
        squiggle()
        squiggle()
        squiggle()
        my_turtle.right(90)
           
#Draws/Fills the sword inside the stamp
def sword():
    #move into place
    my_turtle.penup()
    my_turtle.forward(90)
    my_turtle.left(90)
    my_turtle.forward(20)
    my_turtle.right(90)
    my_turtle.pendown()
    #determines color for fill
    my_turtle.fillcolor("#8f0000")  
    my_turtle.begin_fill()
    #actual sword
    my_turtle.forward(20)
    my_turtle.left(90)
    my_turtle.forward(40)
    my_turtle.right(90)
    my_turtle.forward(15)
    my_turtle.left(90)
    my_turtle.forward(15)
    my_turtle.left(90)
    my_turtle.forward(15)
    my_turtle.right(90)
    my_turtle.forward(80)
    my_turtle.left(45)
    my_turtle.forward(15)
    my_turtle.left(90)
    my_turtle.forward(15)
    my_turtle.left(45)
    my_turtle.forward(80)
    my_turtle.right(90)
    my_turtle.forward(15)
    my_turtle.left(90)
    my_turtle.forward(15)
    my_turtle.left(90)
    my_turtle.forward(15)
    my_turtle.right(90)
    my_turtle.forward(40)
    my_turtle.end_fill()
    #I decided I wanted the metal a different color
    #So I copied and pasted the movement code
    my_turtle.penup()
    my_turtle.color("#ded9d9")
    my_turtle.left(90)
    my_turtle.forward(20)
    my_turtle.left(90)
    my_turtle.forward(40)
    my_turtle.right(90)
    my_turtle.forward(15)
    my_turtle.left(90)
    my_turtle.forward(15)
    my_turtle.left(90)
    my_turtle.forward(15)
    my_turtle.right(90)
    #starts drawing here
    my_turtle.begin_fill()
    my_turtle.pendown()
    my_turtle.forward(80)
    my_turtle.left(45)
    my_turtle.forward(15)
    my_turtle.left(90)
    my_turtle.forward(15)
    my_turtle.left(45)
    my_turtle.forward(80)
    my_turtle.left(90)
    my_turtle.forward(20)
    my_turtle.end_fill()
    my_turtle.color("#000000")
    my_turtle.penup()
    my_turtle.left(180)
    my_turtle.forward(10)
    my_turtle.pendown()
    my_turtle.right(90)
    my_turtle.forward(50)


       
#Combines all the previous funtions into one
def emma_lundquist_stamp(x,y):
     my_turtle.setheading(0)
     stamp_fill(x,y)
     stamp_outline()
     sword()
    
    

def main():
    David_Wheeler_Stamp(300,350)
    David_Wheeler_Stamp(50,50)
    Nathan_Forrer_Stamp(-300,-300)
    Nathan_Forrer_Stamp(100,-150)
    Emma_Lundquist_Stamp(-50,-50)
    
    #stamp (0,175)

main()


