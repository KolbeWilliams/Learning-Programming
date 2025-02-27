#Exercise 3:
import pandas as pd
import numpy as np
from functools import reduce

grades_dict = {'Wally': [86, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
grades.index = ['Test 1', 'Test 2', 'Test 3']
print(grades)
choice_row_column = input('Do you want to calculate min, max, and median for a row or column: ')
choice_num = int(input(f'Which {choice_row_column} do you want to calculate min, max, and median for: '))
if choice_row_column == 'row':
    choice = grades.iloc[choice_num - 1]
elif choice_row_column == 'column':
    choice = grades.iloc[:, choice_num - 1]
print(choice)

minimum = reduce(lambda x, y: x if x < y else y, choice.values)
print(f'The minimum value in that {choice_row_column} is: {minimum}')

maximum = reduce(lambda x, y: x if x > y else y, choice.values)
print(f'The maximum value in that {choice_row_column} is: {maximum}')

choice.values.sort()
median = choice.values[len(choice.values) // 2]
print(f'The median value in that {choice_row_column} is: {median}')