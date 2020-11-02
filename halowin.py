#@Author= lucifer-1010 
# this is the simple python program that wish you the happy hallowin in output
# for more visit my github at https://www.github.cm/Lucifer-1010

import turtle
from turtle import *
t = turtle.Turtle()
t.shape("turtle")
turtle.bgcolor("white")

#Triangle funcution
def make_triangle(x, y, color):
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.color(color)
    t.pendown()
    for count in range(3):
        t.forward(50)
        t.left(120)
    t.end_fill()


#Square function
def make_square(x, y, color):
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.color(color)
    t.pendown()
    for count2 in range(3):
        t.forward(50)
        t.left(60)
    t.end_fill()
t.penup()
t.goto(0, -150)
t.color('#ff6600')
t.begin_fill()
t.circle(150)
t.end_fill()
t.left(180)

# THe teeth:
make_triangle(-35, -20, '#000000')
make_triangle(0, -20, '#000000')
make_triangle(35, -20, '#000000')
make_triangle(70, -20, '#000000')
t.left(180)


# THe eyes:
make_triangle(-70, 50, '#000000')
make_triangle(0, 50, '#000000')


#the stump:
make_square(-20, 125, '#006600')

# happy halloween !
t.penup()
t.goto(-400, -285)
t.write("Happy Hallowin from lucifer-1010", font=("Arial", 36, "normal"))
t.goto(-120, -185)
t.left(120)
turtle.done()
