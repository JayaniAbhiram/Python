from turtle import Turtle,Screen
import prettytable

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.speed()
timmy.color("red","yellow")
timmy.forward(150)
timmy.left(100)
timmy.forward(150)
timmy.right(50)
timmy.forward(150)
timmy.speed(0.5)

myscreen = Screen()
print(myscreen.canvheight)
myscreen.exitonclick()
