from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time

def snake_food():
    food = Turtle()
    food.shape("circle")
    food.color("green")
    food.penup()


###    SCREEN     ###
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake_food()
screen.update()

snake = Snake()

game_on = True
while game_on:
    screen.update()
    time.sleep(0.20)
    snake.moving()





screen.exitonclick()