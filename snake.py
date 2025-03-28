from turtle import Turtle
STARTING_POSITIONS =[(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []   # here we contain the parts of snake body
        self.snake_body()
        self.moving()



    def snake_body(self):

        for position in STARTING_POSITIONS:
            snake = Turtle()
            snake.speed(10)
            snake.shape("square")
            snake.color("orange")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)


    def moving(self):

        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


