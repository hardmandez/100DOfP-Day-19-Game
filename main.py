import random
import turtle
from turtle import Turtle, Screen

screen = Screen()

#Setup screen for game.
# screen.screensize(1200, 1200)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you choose?").lower()
colours = ["red", "blue", "green", "yellow", "purple", "pink"]

turtle_start_x = -225
turtle_start_y = -150

#Setup turtles
for no_of_turtles in range(0,6):
    t = Turtle(shape="turtle")
    t.penup()
    t.color(colours[no_of_turtles])
    t.goto(turtle_start_x, turtle_start_y)
    turtle_start_y += 50

screen.listen()
screen.exitonclick()


