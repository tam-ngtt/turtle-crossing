from turtle import Turtle
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.starting_pos()

    def starting_pos(self):
        self.goto(x=0, y=-280)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_game(self):
        self.starting_pos()
