from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class GameBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("score.txt", mode="r") as data:
            self.high_score= int(data.read())
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}   High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def reset_score_board(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score_board()
