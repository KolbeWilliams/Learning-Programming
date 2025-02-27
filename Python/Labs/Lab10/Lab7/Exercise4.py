#Exercise 4: Flatten the 2x4 array from the last problem using a deep copy. Create a series using the elements
#in this flattened array.Print the series and produce descriptive statistics.
import numpy as np
import pandas as pd

grades = np.zeros((2, 4))
for row in range(len(grades)):
    for column in range(len(grades[0])):
        grades[row][column] = int(input('Enter grade: '))

print('\nGrades:\n', grades)
grades_flattened = grades.flatten()
print('\nGrades array flattened:\n', grades_flattened)
semesterGrades = pd.Series(grades_flattened)
print('\nSeries:\n', semesterGrades)
print('\nDescriptive Statistics:\n', semesterGrades.describe())