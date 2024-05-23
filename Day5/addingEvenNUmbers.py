rangeOfNumbers = int(input("enter the range of numbers you wanna add : "))

total = 0
for number in range (0 , rangeOfNumbers+1,2):
    total = total + number

print(total)