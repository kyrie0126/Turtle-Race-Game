# Day 19 of 100 days of code
# instances, states, and higher order functions
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=800, height=400)
screen.title("Welcome to the turtle race!")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


all_turtles = []
for i in range(0, 6):
    timmy = Turtle()
    timmy.penup()
    timmy.shape("turtle")
    timmy.color(colors[i])
    timmy.goto(x=-385, y=-125+50*i)
    all_turtles.append(timmy)


bet = screen.textinput(title="Place Your Bet", prompt="Which color turtle is going to win?").lower()


if bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 360:
            winner_color = turtle.color()[0]
            is_race_on = False

        step = random.randint(0, 10)
        turtle.forward(step)

if winner_color == bet:
    print(f" The winner is {winner_color}. You win!")
else:
    print(f"The winner is {winner_color}. You lose!")

screen.exitonclick()

