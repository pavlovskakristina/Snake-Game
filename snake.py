from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN =270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []   # here we contain the parts of snake body
        self.snake_body()
        self.head = self.segments[0]

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
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

