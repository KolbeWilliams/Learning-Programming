#Exercise 1:
HWname = []
HWgrade = []
num_grades = int(input('How many homework grades do you want to enter: '))
for x in range(num_grades):
    name = input('Enter a name: ')
    HWname.append(name)
    grade = int(input(f"Enter {name}'s grade: "))
    HWgrade.append(grade)
GradesDictionary = {}
for x in range(num_grades):
    GradesDictionary[HWname[x]] = HWgrade[x]
print(GradesDictionary)