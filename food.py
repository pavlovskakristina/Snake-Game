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
        X_POS = random.choice(range(-280, 280, 20))
        Y_POS = random.choice(range(-280, 280, 20))
        print(X_POS, Y_POS)
        self.goto(X_POS, Y_POS)
        pass

"""    def lost_the_game(self):
        # collision with wall

        # collision with tail

        pass"""