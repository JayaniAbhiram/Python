import math


def dimensions(height,width):
    height = str(height)
    width = str(width)
    
    print("height of the wall is " + height)
    print("width of the wall is"+ width)


height = int(input("enetr the height of the wall: "))
width = int(input("enter the width of the wall : "))

area = (height*width)

def paintCans():
    cans = area/5
    cans = math.ceil(cans)
    print(area)
    print(cans)

dimensions(height,width)
paintCans()

