#Exercise 2: Using exercise 1, create 5 lists from the panda series, one for each grade (A-F).
#Create a pic chart where the slices are the number of elements in each of the lists. For colors,
#use r, g, b, y, m, start at 90?, use shadow, and explode the F grades in the pie chart
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

grades = []
end = 1
while(end):
    grade = float(input('Enter a grade or enter a negative number to stop: '))
    if grade < 0:
        end = 0
    else:
        grades.append(grade)
gradesArr = np.array(grades)
indicies = [x for x in range(1, len(grades) + 1)]
gradesSeries = pd.Series(gradesArr, indicies)
print(f'\n{gradesSeries.describe()}')
A = list(gradesSeries[(gradesSeries >= 90) & (gradesSeries <= 100)])
B = list(gradesSeries[(gradesSeries >= 80) & (gradesSeries < 90)])
C = list(gradesSeries[(gradesSeries >= 70) & (gradesSeries < 80)])
D = list(gradesSeries[(gradesSeries >= 60) & (gradesSeries < 70)])
F = list(gradesSeries[(gradesSeries < 60)])
numElements = [len(A), len(B), len(C), len(D), len(F)]
plt.pie(numElements, labels = ['A', 'B', 'C', 'D', 'F'], 
        colors = ['r', 'g', 'b', 'y', 'm'], 
        startangle= 90,
        shadow = True,
        explode = (0, 0, 0, 0, 0.1),
        autopct = '%1.1f%%')
plt.show()
