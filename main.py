from turtle import Screen
from snake import Snake
from food import Food
from score_board import GameBoard
import time


#    SCREEN     #
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
gameboard = GameBoard()

# Controling the game by the keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.10)
    snake.moving()

    # +1 Segment - Collision with the food
    if snake.head.distance(food) < 15:
        gameboard.increase_score()
        food.random_appearing()
        snake.extend()

    # GAME OVER - Collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameboard.reset_score_board()
        snake.reset()

    # GAME OVER - Collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameboard.reset_score_board()
            snake.reset()

screen.exitonclick()
