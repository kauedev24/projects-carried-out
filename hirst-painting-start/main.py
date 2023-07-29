###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle as t
from random import choice


rgb_colors = []
colors = colorgram.extract('/home/user/AreaTrabalho/100daysofpython/hirst-painting-start/image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)


tim = t.Turtle()
t.colormode(255)
tim.pensize(15)
tim.speed(0)
tim.hideturtle()


def points():
    tim.up()
    tim.down()
    tim.forward(0)
    tim.up()
    tim.forward(50)
    tim.down()
    tim.forward(0)


stop = 0
y = 300
while True:
    tim.up()
    tim.setpos(-270, y)

    for i in range(9):
        tim.pencolor(choice(rgb_colors))
        points()
       
    y -= 30

    stop += 1
    if stop == 10:
        break


screen = t.Screen()
screen.exitonclick()