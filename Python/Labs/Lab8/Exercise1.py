#Exercise 1:
import pandas as pd

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
index1 = input('Enter the name of the first index: ')
index2 = input('Enter the name of the second index: ')
index3 = input('Enter the name of the third index: ')
grades.index = [index1, index2, index3]

choice_rc = input('Do you want to sort by rows or columns: ')
choice_direction = input('Do you want to sort in ascending or descending order: ')
while choice_rc.lower() == 'rows' and choice_direction.lower() == 'ascending':
    print(grades.sort_index(axis = 0))
    break
while choice_rc.lower() == 'rows' and choice_direction.lower() == 'descending':
    print(grades.sort_index(axis = 0, ascending = False))
    break
while choice_rc.lower() == 'columns' and choice_direction.lower() == 'ascending':
    print(grades.sort_index(axis = 1))
    break
while choice_rc.lower() == 'columns' and choice_direction.lower() == 'descending':
    print(grades.sort_index(axis = 1, ascending = False))
    break