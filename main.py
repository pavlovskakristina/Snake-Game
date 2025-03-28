from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time


###    SCREEN     ###
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

screen.update()

snake = Snake()
food = Food()

screen.listen()    # Listening the key and moving
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_on = True
while game_on:
    screen.update()
    time.sleep(0.10)
    snake.moving()
#    food.random_appearing()
#    Ta linijka kodu sprawia to, że z każdym
#    przesunięciem węża food zmienia randomowo swoją lokalizację


    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False






screen.exitonclick()
