import random

randomNum = random.randint(0,100)

print(randomNum)
difficulty = input("choose the difficulty level easy or hard : ")


if difficulty == "easy":
    count = 10
    print("you have " + str(count) + " chances to guess")
    end = False
    while not end:
        guess = int(input("guess a number : "))
        if guess > randomNum:
            count = count-1
            # print(count)
            print("too high ,, guess a smaller one")
            if count <= 0:
                print("you are out of chances,,  you loose")
                end = True
        elif guess < randomNum:
            count = count-1
            # print(count)
            print("too low ,, guess a greater one")
            if count <= 0:
                print("you are out of chances,,  you loose")
                end = True
        
        else:
            print("you guessed right")
            end = True

if difficulty == "hard":
    count = 5
    print("you have " + str(count) + " chances to guess")
    end = False
    while not end:
        guess = int(input("guess a number : "))
        if guess > randomNum:
            count = count-1
            # print(count)
            print("too high ,, guess a smaller one")
            if count <= 0:
                print("you are out of chances,,  you loose")
                end = True
        elif guess < randomNum:
            count = count-1
            # print(count)
            print("too low ,, guess a greater one")
            if count <= 0:
                print("you are out of chances,,  you loose")
                end = True

        else:
            print("you guessed right")
            end = True
    



        
    


