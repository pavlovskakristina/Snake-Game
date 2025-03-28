import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.penup()
        self.random_appearing()

    def random_appearing(self):
        x_pos = random.choice(range(-280, 280, 20))
        y_pos = random.choice(range(-280, 280, 20))
        self.goto(x_pos, y_pos)

