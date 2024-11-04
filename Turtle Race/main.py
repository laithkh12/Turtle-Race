from turtle import Turtle, Screen
isRaceOn = False
import random


screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bit", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yPositions = [-70, -40, -10, 20, 50, 80]
allTurtles = []

for turtleIndex in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[turtleIndex])
    newTurtle.penup()
    newTurtle.goto(x= -230, y= yPositions[turtleIndex])
    allTurtles.append(newTurtle)

if userBet:
    isRaceOn = True

while isRaceOn:

    for turtle in allTurtles:
        if turtle.xcor() > 230:
            isRaceOn = False
            winningTurtle = turtle.pencolor()
            if winningTurtle == userBet:
                print(f"You have won, The {winningTurtle} turtle is the winner!")
            else:
                print(f"You have lost, The {winningTurtle} turtle is the winner!")
        randDistance = random.randint(0, 10)
        turtle.forward(randDistance)








screen.exitonclick()