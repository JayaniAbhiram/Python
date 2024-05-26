import os

def clearConsole():
    os.system("cls")

entries = {}

def highestBid():
    highest_bid = 0
    winner = ""
    for bidder in entries:
        bid_amount = entries[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is: {winner}")
    print(f"The amount bidded is: ${highest_bid}")

def details():
    name = input("Enter your name: ")
    bid = int(input("Enter how much you want to bid: $"))  
    entries[name] = bid

details()

end = False
while not end:
    verify = input("Are there any other bidders? Type yes or no: ").lower()
    if verify == "yes":
        clearConsole()
        details()
    else:
        print("Bye")
        end = True

highestBid()
