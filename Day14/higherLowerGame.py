import random

from gameData import data

points = 0
end = False
while not end:
    randomData1 = random.choice(data)
    randomData2 = random.choice(data)
    if randomData1 == randomData2:
        randomData2 = random.choice(data)

    check1 = randomData1["follower_count"]
    name1 = randomData1["name"]
   
    check2 = randomData2["follower_count"]
    name2 = randomData2["name"]

    choosing = input("choose " + name1 +" or "+ name2 + " " )

    
    if choosing == name1:
        if check1>check2:
            print(name1 + "has " + str(check1) + " count and " + name2 + " has " + str(check2) + " count"  )
            points = points+1
            continueGame = input("do u wanna continue: yes or no")
            if continueGame == "no":
                end =True
            # print(points)
        elif check1<check2:
            print(name2 + "has " + str(check2) + " countand " + name1 + " has " + str(check1) + " count")
            points = points-1
            # print(points)
            if points <0 :
                print("you loose")
                end = True
    
                
    if choosing == name2:
        if check2>check1:
            print(name2 + "has " + str(check2) + " count and " + name1 + " has " + str(check1) + " count")
            points = points+1
            continueGame = input("do u wanna continue: yes or no")
            if continueGame == "no":
                end =True
            # print(points)
        elif check2<check1:
            print(name1 + "has " + str(check1) + " count and " + name2 + " has " + str(check2) + " count")
            points = points-1
            # print(points)
            if points < 0 :
                print("you loose")
                end = True
    
    # continueGame = input("do u wanna continue: yes or no")
    # if continueGame == "no":
    #     end =True

    
print(points)







    