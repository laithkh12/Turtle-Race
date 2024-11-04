# Turtle Race Betting Game

This project is an interactive game built with Python's Turtle graphics library. Players place a bet on which turtle will win the race, and then watch as the turtles compete! 

## Features
- **Place a Bet** - Choose a turtle color and place a bet on which one you think will win.
- **Randomized Race** - Each turtle progresses forward by a random distance, making each race unpredictable.
- **Result Notification** - At the end of the race, the program announces if your chosen turtle won or lost.

## Code Overview

### Importing Modules
We use the `turtle` module for graphics, along with `random` for generating random race distances.

```python
from turtle import Turtle, Screen
import random

# Setting Up the Screen
screen = Screen()
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bit", prompt="Which turtle will win the race? Enter a color: ")

# Turtles and Positions
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yPositions = [-70, -40, -10, 20, 50, 80]
allTurtles = []

# Each turtle is created and positioned using a for loop.
for turtleIndex in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[turtleIndex])
    newTurtle.penup()
    newTurtle.goto(x= -230, y= yPositions[turtleIndex])
    allTurtles.append(newTurtle)

# Starting the Race
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

# Exiting the Program
screen.exitonclick()
```

## Requirements
- Python 3.x
- Turtle graphics library (standard in Python)

## How to Run
1. Clone the repository or download the script.
2. Run the program with:
```bash
python turtle_race_game.py
```
3. Follow the on-screen instructions to place your bet and watch the race.

## License
- This project is open-source and available under the MIT License.




Have fun betting on your favorite turtle and good luck!
