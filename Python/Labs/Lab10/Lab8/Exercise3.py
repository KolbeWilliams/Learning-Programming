#Exercise 3:
import pandas as pd
from matplotlib import pyplot as plt

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
index1 = input('Enter the name of the first index: ')
index2 = input('Enter the name of the second index: ')
index3 = input('Enter the name of the third index: ')
grades.index = [index1, index2, index3]

names = list(grades.columns)
plt.boxplot(grades)
plt.title('Student Grades')
plt.xlabel('Students')
plt.ylabel('Grades')
plt.xticks([x + 1 for x in range(len(names))], [name for name in names])
plt.show()