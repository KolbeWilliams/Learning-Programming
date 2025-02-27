#Exercise 1: Using an infinite loop, enter at least 10 grades into a grades list and break the
#loop when the user enters a grade smaller than 0. Create a numpy array out of the grades list
#and create an Panda series out of the numpy array and rename indicies to begin at 1 (use list
#comprehension). Print the descriptive statistice of the grades. Create 3 plots in a single graph 
#(plot, scatter, and bar). x-axis indicies will begin with 1 and y-axis is grades entered.
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

x_values = indicies
y_values = grades
plt.plot(x_values, y_values)
plt.scatter(x_values, y_values)
plt.bar(x_values, y_values, color = 'tab:orange')
plt.ylim(0, 100)
plt.show()