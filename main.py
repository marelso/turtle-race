from turtle import *


def draw_speedway():
    speed(5)
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
