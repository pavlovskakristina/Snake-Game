from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.game_over()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_score_board()


    def update_score_board(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
