students = [10,11,12,13,14,15]
numberOfStudents = len(students)

totalHeight = 0
for height in students:
    totalHeight = totalHeight + height
print(totalHeight)

# for average height

averageHeight = totalHeight/numberOfStudents
print(averageHeight)