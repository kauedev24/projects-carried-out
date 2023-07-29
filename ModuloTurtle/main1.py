from turtle import Screen
import turtle as t
from random import choice, randint


kauerva = t.Turtle()
t.colormode(255)
kauerva.speed(10)
kauerva.shape('turtle')
kauerva.pensize(15)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb

directions = [0, 90, 180, 270]  # 0>>east / 90>>north / 180>>oeste / 270>>sul
# colors = ['lime green', 'orange red', 'purple', 'gold', 'lime green', 'black', 'deep sky blue']


for i in range(200):
    kauerva.pencolor(random_color())
    kauerva.forward(50)
    kauerva.setheading(choice(directions))

    # kauerva.right(choice(directions))
    # kauerva.left(choice(directions))










screen = Screen()
screen.exitonclick()

