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


def create_turtle(color, coords):
    turtle = Turtle()
    turtle.color(color)
    turtle.shape('turtle')
    turtle.penup()
    turtle.goto(coords[0], coords[1])
    turtle.pendown()
    return turtle


def turn(turtles):
    for turn in range(100):
        for turtle in turtles:
            turtle.forward(randint(1, 5))


def start(competitors):
    base = 100
    turtles = []

    for id in range(competitors):
        color = input("Choose a color for the turtle:")

        turtles.append(create_turtle(color, [-160, base]))
        base -= 30

    return turtles


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    turtles = start(int(input("Choose the number of competitors:")))

    draw_speedway()

    turn(turtles)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
