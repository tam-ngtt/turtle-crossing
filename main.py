from turtle import Screen
from car import Car
from player import Player
from scoreboard import ScoreBoard
import time

"""Screen Setup"""
screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.title("Turtle Crossing Road")
screen.tracer(0)

car = Car()
scoreboard = ScoreBoard()
screen.update()
player = Player()
screen.listen()
screen.onkey(key="Up", fun=player.move)
screen.onkey(key="space", fun=player.move)


game_is_on = True
starting_pace = 0.1
while game_is_on:
    time.sleep(starting_pace)
    screen.update()

    # Detect the turtle crossing the finishing line
    if player.ycor() > 280:
        scoreboard.score += 1
        scoreboard.update_score()
        player.reset_game()
        starting_pace *= 0.9
        car.increase_speed()

    """Create multiple cars crossing the road"""
    car.create_car()
    car.move()

    # Detect collision with cars
    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
