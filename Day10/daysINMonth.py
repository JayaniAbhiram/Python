

def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
                # print("it is a leap year")
            else:
                return False
                # print("not a leap year")
        else:
            return True
            # print("it is a leap year")
    else:
        return False
    # print("not a leap year")
def daysOfMonth(year,month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and isLeapYear(year):
        return 29
    else:
        days = monthDays[month-1]
        return days

year = int(input("enter a year: "))
month = int(input("enter the month: "))
days = daysOfMonth(year,month)
print(days)