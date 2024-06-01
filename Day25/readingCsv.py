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
# print(type(data["temp"]))

# changing the excel data into dictionary
dataDict = data.to_dict()
print(dataDict)

#  print(dataDict["temp"])

tempList = data["temp"].to_list()
print(tempList)


# to fing the avegrage temperature
totalTemp = 0
for temp in tempList:
    totalTemp = totalTemp + temp

print(totalTemp)
avgTemp = totalTemp / len(tempList)
print(avgTemp)

# or one more methoud using the sum inbuild method

totalTemp = sum(tempList)
print(totalTemp/ 7)


print(data["temp"].mean())
maxTemp = data["temp"].max()


print(data[data.temp == data.temp.max()])

# creating our own dataframe

datadict = {
    "students": ["skfdjhvbsk","lfdjgkvndk","iywegfyuwer"],
    "roll number":[15,20,25]
}

newcsv = pandas.DataFrame(datadict)
newcsv.to_csv("createdCsv.csv")