subjects = ["sinhala","English","ICT","Maths"]
marks = []
grades = []
total = 0
average = 0

def gradeCal(mark):
    if mark >= 75:
        return "A"
    elif mark >= 65:
        return "B"
    elif mark >= 55:
        return "C"
    elif mark >= 35:
        return "S"
    else:
        return"W"

for subject in subjects:
    mark = int(input("Enter marks for "+ subject + ": "))
    marks.append(mark)
    total = total + mark
    grades.append(gradeCal(mark))

for i in range(len(subjects)):
    print(subjects[i]," - " , marks[i], " - ", grades[i])

print("total = ",total)
print("Average = ", total/len(subjects))

