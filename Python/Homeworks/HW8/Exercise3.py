#Exercise 3:
import pandas as pd
from matplotlib import pyplot as plt

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
grades.index = ['Test 1', 'Test 2', 'Test 3']
print(grades)

x_values = list(grades.keys())
plt.plot(x_values, grades.loc['Test 1'], 'r--*', label = 'Test 1')
plt.plot(x_values, grades.loc['Test 2'], 'g-.*', label = 'Test 2')
plt.plot(x_values, grades.loc['Test 3'], 'b-*', label = 'Test 3')
plt.xlabel('Student Names')
plt.ylabel('Grades')
plt.title('Student Grades')
plt.ylim(0, 100)
plt.legend()
plt.show()