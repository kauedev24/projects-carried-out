from turtle import Turtle, Screen


mouse = Turtle()
screen = Screen()
screen.listen()

def up_():
    mouse.forward(10)


def down_():
    mouse.backward(10)


def turn_right():
    mouse.right(10)


def turn_left():
    mouse.left(10)


def clear_():
    screen.resetscreen()


while True:
    screen.onkey(up_, 'w')
    screen.onkey(down_, 's')
    screen.onkey(turn_right, 'd')
    screen.onkey(turn_left, 'a')
    screen.onkey(clear_, 'c')


    if screen.exitonclick():
        break
