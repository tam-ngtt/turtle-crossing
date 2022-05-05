from turtle import Turtle
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(x=-280, y=260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level:{self.score}", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", font=FONT, align="center")

