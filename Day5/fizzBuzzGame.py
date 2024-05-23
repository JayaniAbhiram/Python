rangeOfCount = int(input("enter the range of number which shoukd be considered:"))

for number in range(1,rangeOfCount+1):
    if number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    print(number)