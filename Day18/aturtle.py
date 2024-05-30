from turtle import Turtle, Screen
 

timmy = Turtle()
timmy.shape("turtle")
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

timmy.forward(150)
timmy.left(160)
timmy.forward(120)
for i in range(10):
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)


















screen = Screen()
screen.exitonclick()