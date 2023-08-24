from turtle import Turtle, Screen
import random

color_choice = ['red', 'blue', 'yellow', 'cyan', 'magenta', 'orange', 'brown', 'grey', 'purple', 'black', 'salmon']


t = Turtle()
t.speed('fastest')
t.up()
t.setx(-200)
t.sety(-200)
t.hideturtle()


def turtle_move():
    for n in range(10):
        t.up()
        t.begin_fill()
        t.dot(20, random.choice(color_choice))
        t.end_fill()
        t.up()
        t.forward(40)
        t.down()


for i in range(10):
    turtle_move()
    t.up()
    t.setx(-200)
    t.left(90)
    t.forward(40)
    t.right(90)


myScreen = Screen()
myScreen.exitonclick()
