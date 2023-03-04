from turtle import *
from random import randint

drawing_speed = 20


def draw_speedway():
    speed(drawing_speed)
    penup()
    goto(-140, 140)
    for step in range(16):
        write(step, align='center')
        right(90)
        forward(10)
        pendown()
        forward(150)
        penup()
        backward(160)
        left(90)
        forward(20)


def create_turtle(color, x, y):
    turtle = Turtle()
    turtle.color(color)
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    return turtle


def turn(turtles):
    for turn in range(100):
        turtles[0].forward(randint(1,5))
        turtles[1].forward(randint(1,5))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    turtles = []
    draw_speedway()

    erica = create_turtle('green', -160, 100)
    marelso = create_turtle('blue', -160, 70)

    turtles.append(erica)
    turtles.append(marelso)

    turn(turtles)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
