from turtle import Turtle, Screen
from random import choice

def triangle():
    for i in range(3):
        tim.forward(100)
        tim.right(120)
    

def square():
    for i in range(4):
        tim.forward(100)
        tim.right(90)


def pentagon():
    for i in range(5):
        tim.forward(100)
        tim.right(72)
    

def hexagon():
    for i in range(6):
        tim.forward(100)
        tim.right(60)


def heptagon():
    for i in range(7):
        tim.forward(100)
        tim.right(51.4)
     

def octagon():
    for i in range(8):
        tim.forward(100)
        tim.right(45)
    

def nonagon():
    for i in range(9):
        tim.forward(100)
        tim.right(40)
    

def decagon():
    for i in range(10):
        tim.forward(100)
        tim.right(36)


tim = Turtle()
tim.shape('turtle')
tim.color('NavyBlue')

colors = ['lime green', 'orange red', 'purple', 'gold', 'lime green', 'black', 'deep sky blue']

for i in range(8):
    tim.pencolor(choice(colors))
    
    # tim.speed(1)
    if i == 0:
        triangle()
    if i == 1:
        square()
    if i == 2:
        pentagon()
    if i == 3:
        hexagon()
    if i == 4:
        heptagon()
    if i == 5:
        octagon()
    if i == 6:
        nonagon()
    if i == 7:
        decagon()
     

screen = Screen()
# screen.bgcolor('orange')
screen.exitonclick()