print("Hii Welcome to the treasure island game")
print("\n""Choose left or right")
firstInput = input()
if (firstInput == "left"):
    print("you entered into next level")
    print("choose swim or wait")
    secondInput = input()
    if (secondInput == "swim"):
        print("Game Over")
    elif(secondInput == "wait"):
        print("you have entered into next level")
        print("choose red or blue or yellow")
        thirdInput = input()
        if(thirdInput == "red"):
            print("Game over")
        elif(thirdInput == "blue"):
            print("Game over")
        elif(thirdInput == "yellow"):
            print("you win !!")
        else:
            print("choose only from red or yellow or blue")
    else:
        print("choose from between swim or wait only")   
elif (firstInput == "right"):
    print("Game over")
else:
    print("choose between only left or right")


