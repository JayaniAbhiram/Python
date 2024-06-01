import pandas

data = pandas.read_csv("Python\\Day25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240531.csv")

greySqirils = data[data["Primary Fur Color"] == "Gray"]
redSqirils = data[data["Primary Fur Color"] == "Cinnamon"]
whiteSqirils = data[data["Primary Fur Color"] == "Whitw"]
# print(greySqirils)

greysquirilsCount = len(greySqirils)
redsquirilsCount = len(redSqirils)
whitesquirilsCount = len(whiteSqirils)
# print(len(data["Primary Fur Color"] == "Grey"))
# print(len(data["Primary Fur Color"] == "Grey"))
# print(len(data["Primary Fur Color"] == "Grey"))

dataDict = {
    "furColor" : ["Cinnamon", "Gray ", "White"],
    "count": [redsquirilsCount,greysquirilsCount,whitesquirilsCount]
}

newCsv = pandas.DataFrame(dataDict)
newCsv.to_csv("colorcount.csv")

