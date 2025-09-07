import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
#Setup screen for game.
# screen.screensize(1200, 1200)
screen.setup(width=500, height=400)

colours = ["red", "blue", "green", "yellow", "purple", "pink"]
turtle_rotation=[36,72,108,144,180,216,252,288,324,360,0]
turtle_start_x = -225
turtle_start_y = -((400/7))*2
finish_line_x = 220
race_on = False
all_turtles=[]
finish_order=[]

#Setup turtles
for no_of_turtles in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[no_of_turtles])
    for _ in turtle_rotation:
        new_turtle.speed(100)
        new_turtle.setheading(_)
    new_turtle.speed(2)
    new_turtle.goto(turtle_start_x, turtle_start_y)
    turtle_start_y += 50
    all_turtles.append(new_turtle)

#Get bet.
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle do you choose?").lower()

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        race_distance = random.randint(0,10)
        turtle.forward(race_distance)
        if turtle.xcor() >= finish_line_x:
            all_turtles.remove(turtle)
            finish_order.append(turtle)

        if not all_turtles:
            race_on = False


if user_bet == finish_order[0].colo:
    print("You win!")
else:
    print("You lose!")
    print(f"{finish_order[0]} wins.")

screen.listen()
screen.exitonclick()


