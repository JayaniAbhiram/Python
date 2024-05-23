import random
import string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

forLetters = int(input("enter the number of letters to be inclided in the password: "))
forNumbers = int(input("enter the number of numbers to be inclided in the password: "))
forSymbols = int(input("enter the number of symbols to be included in the password: "))

# for letter in range(0, forLetters):
#     letters = random.randint(letters)
#     print(letters)

password = ""
for char in range(0,forLetters):
    randomChar = random.choice(letters)
    # print(randomChar)

    password = password + randomChar
print(password)

for char in range(0, forNumbers):
    randomChar = random.choice(numbers)

    password = password + randomChar

print(password)

for char in range(0, forSymbols):
    randomChar = random.choice(symbols)

    password = password + randomChar

print(password)


passwordSplit = list(password)
print(passwordSplit)

print("changint to the random passwords")

newPassword = random.sample(passwordSplit,len(passwordSplit))
print(newPassword)