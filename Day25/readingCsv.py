# with open("Python\Day25\weather_data.csv") as dataFile:
#     data = dataFile.readlines()
#     print(data)

# import csv

# with open("Python\Day25\weather_data.csv") as dataFile:
#     data = csv.reader(dataFile)
#     temperatures = []
#     print(data)
#     for row in data:
#         print(row)
#         if row[1] != "temp":
        
#             temperatures.append(row[1])
#     print(temperatures)




# by using pandas

import pandas
data = pandas.read_csv("Python\Day25\weather_data.csv")
print(data["temp"])
