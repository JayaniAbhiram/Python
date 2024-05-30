from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()



def moveLeft():
    timmy.left(30)

def moveRight():
    timmy.right(30)
    # timmy.setheading(20)
def moveForward():
    timmy.forward(20)
def moveBack():
    timmy.left(180)










screen.listen()
screen.onkey(key = "a", fun=moveLeft)
screen.onkey(key="w", fun=moveForward)
screen.onkey(key="d", fun=moveRight)
screen.onkey(key="s", fun=moveBack)

screen.exitonclick()
