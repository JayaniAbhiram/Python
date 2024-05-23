import random
print("choose 0 for rock and 1 for paper and 2 for scissor\n")
user_choice = int(input())

comp_choice = random.randint(0, 2)
print(comp_choice)
if (user_choice == 0 and comp_choice == 1):
    print("You lose")
elif(user_choice == 0 and comp_choice == 2):
    print("You Won")
elif(user_choice == 1 and comp_choice == 2):
    print("you loose")
elif(user_choice == 1 and comp_choice == 0):
    print("you win")
elif(user_choice == 2 and comp_choice == 0):
    print("you loose")
elif(user_choice == 2 and comp_choice == 1):
    print("you won")
elif(user_choice == comp_choice):
    print("its a draw")
else:
    print("enter a valid number for the choice")