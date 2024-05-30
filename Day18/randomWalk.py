from turtle import Turtle, Screen
import random

timmy = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

directions = [ 0,90,180,270]
timmy.pensize(4)
timmy.speed(30)




for i in range(330):
    # timmy.forward(random.choice(directions))
    # timmy.left(random.choice(directions))
    # timmy.right(random.choice(directions))
    timmy.color(random.choice(colours))
    timmy.forward(20)
    timmy.setheading(random.choice(directions))
    
  









Screen = Screen()
Screen.exitonclick()