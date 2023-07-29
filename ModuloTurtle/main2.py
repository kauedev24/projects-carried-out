import turtle as t
from random import randint

motta = t.Turtle()
t.mode('logo')
motta.home()
t.colormode(255)
motta.speed(0)
range_ = 36  # valor dado para movimento de 10°, caso altere esse valor, deve-se considerar alterar o range(diminuir grau caso aumente range).

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb


for i in range(range_):
    motta.color(random_color())
    motta.circle(100)
    motta.left(10)



screen = t.Screen()
screen.exitonclick()