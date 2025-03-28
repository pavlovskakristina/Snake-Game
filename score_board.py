
class Game_Board:

    def __init__(self):
        self.game_over()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGMENT, font=FONT)