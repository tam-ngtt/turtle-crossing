from turtle import Turtle
from random import randint
MOVING_DISTANCE = 5
INCREASE_SPEED = 2


class Car:
    def __init__(self):
        self.all_cars = []
        self.move_speed = MOVING_DISTANCE

    def create_car(self):
        """Create a car approximately every six times."""
        chance = randint(1, 6)
        if chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color((randint(1, 255), randint(1, 255), randint(1, 255)))
            new_car.goto(300, randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    def increase_speed(self):
        self.move_speed += INCREASE_SPEED



