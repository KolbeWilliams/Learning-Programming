#Exercise 2:
import pandas as pd

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
index1 = input('Enter the name of the first index: ')
index2 = input('Enter the name of the second index: ')
index3 = input('Enter the name of the third index: ')
grades.index = [index1, index2, index3]
choice_rc = input('Do you want to sort by rows or columns: ')
if choice_rc.lower() == 'rows':
    choice_name_assignment = input('What student do you want to sort by: ')
elif choice_rc.lower() == 'columns':
    choice_name_assignment = input('What assignment do you want to sort by: ')
else:
    print('Invalid input')
choice_direction = input('Do you want to sort in ascending or descending order: ')
if choice_direction.lower() == 'ascending':
    choice_direction = True
elif choice_direction.lower() == 'descending':
    choice_direction = False
else:
    print('Invalid input')
print(grades.sort_values(by = choice_name_assignment, axis = 0 if choice_rc == 'rows' else 1, ascending = choice_direction))