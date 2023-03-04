from turtle import *
from random import randint
import tkinter as tk


class NumberField(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.number_var = tk.StringVar()

        tk.Label(self, text="Number:").grid(row=0, column=0)
        tk.Entry(self, textvariable=self.number_var).grid(row=0, column=1)

        tk.Button(self, text="Next", command=self.show_text_fields).grid(row=1, column=0, columnspan=2, pady=10)

    def show_text_fields(self):
        num = int(self.number_var.get())
        self.master.withdraw()  # hide NumberField window
        TextFields(self.master, num, self.on_start)

    def on_start(self, values):
        print(f"Start button clicked with values: {values}")

        turtles = start(values)

        draw_speedway()

        turn(turtles)
        # ... do something with values ...


class TextFields(tk.Toplevel):
    def __init__(self, parent, num, on_start):
        super().__init__(parent)

        self.text_vars = []
        self.on_start = on_start

        for i in range(num):
            var = tk.StringVar()
            tk.Label(self, text=f"Text {i + 1}:").grid(row=i, column=0)
            tk.Entry(self, textvariable=var).grid(row=i, column=1)
            self.text_vars.append(var)

        tk.Button(self, text="Start", command=self.do_start).grid(row=num, column=0, columnspan=2, pady=10)

    def do_start(self):
        values = [var.get() for var in self.text_vars]
        self.on_start(values)
        self.destroy()  # close TextFields window
        self.master.deiconify()  # show NumberField window again


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

    for id in range(len(competitors)):
        color = competitors[id]

        turtles.append(create_turtle(color, [-160, base]))
        base -= 30

    return turtles


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("300x200")

    number_field = NumberField(root)
    number_field.pack(fill="both", expand=True)

    root.mainloop()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
