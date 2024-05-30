from turtle import Turtle, Screen
import random


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

screen = Screen()
screen.setup(width=400,height=400)
userBet = screen.textinput(title="Make a bet",prompt="Choose the color of the turtle")
print(userBet)
screen.exitonclick()

isRaceOn = False

yPosition = [-150,-120,-90,-60,-30,0,+30,+60,+90,+120]
turtles =[]

for turle in range(9):
    tim = Turtle(shape="turtle")
    tim.color(random.choice(colours))
    tim.penup()
    tim.goto(x=-160,y=yPosition[turle])
    turtles.append(tim)


while not isRaceOn:
    for turtle in turtles:
        randomDistance = random.randint(5,15)
        turtle.forward(randomDistance)
        
        if turtle.xcor() > 230:
            winningColor = turtle.pencolor()
            if winningColor == userBet:
                print("the winner is" + userBet)
           
        
          


















