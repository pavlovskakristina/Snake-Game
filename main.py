from turtle import Turtle, Screen
#import random
import time

segments = []    # here we contain the parts of snake body

def snake_body():
    x_position = 0
    for _ in range(3):
        snake = Turtle()
        snake.speed(10)
        snake.shape("square")
        snake.color("orange")
        snake.penup()
        segments.append(snake)
        snake.goto(x=x_position, y =0)
        x_position -= 20


def snake_food():
    food = Turtle()
    food.shape("circle")
    food.color("green")
    food.penup()




###    SCREEN -- activity    ###
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake_body()
snake_food()
screen.update()


game_on = True
while game_on:
    screen.update()
    # To nie symuluje naturalnego ruchu węża – wszystkie segmenty idą na raz, zamiast podążać za głową. Potrzebna będzie dodatkowa logika.
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)








screen.exitonclick()