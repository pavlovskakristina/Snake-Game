from turtle import Turtle
from random import *

class Food:

    def __init__(self):
        self.food()
        self.random_appearing(self)


    def food(self):
        food = Turtle()
        food.shape("circle")
        food.color("green")
        food.penup()


    def random_appearing(self):
        pass