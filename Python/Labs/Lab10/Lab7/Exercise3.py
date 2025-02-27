#Exercise 3: Creat a 2x4 numpy array filled with zeros. Ask user for grades to fill the array.
#Create a series using a dictionary. Ask user which semster to plot. Also ask for line width and 
#case insensitive color. Add title, xlabel, ylabel.
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

grades = np.zeros((2, 4))
for row in range(len(grades)):
    for column in range(len(grades[0])):
        grades[row][column] = int(input('Enter grade: '))

print('Grades:\n', grades)
semesterDictionary = {'Fall': grades[0, :], 'Spring': grades[1, :]}
semesterGrades = pd.Series(semesterDictionary)
semester = input('Which semester do you wish to plot: ')
print('Grades for fall: ', semesterGrades[semester])
lineWidthChoice = int(input('Linewidth: '))
lineColorChoice = input('Line Color: ')
x = range(len(semesterGrades[semester]))
plt.plot(x , semesterGrades[semester], color = lineColorChoice.lower(), linewidth = lineWidthChoice)
plt.title(f'{semester} Semester Grades')
plt.xlabel(f'{semester}')
plt.ylabel('Grades')
plt.xticks(x)
plt.show()