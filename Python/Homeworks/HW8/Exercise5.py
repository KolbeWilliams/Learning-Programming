#Exercise 5:
import pandas as pd

def sort_function(DF, data, choice):
    sorted_data = []
    while len(data) != 0:
        lowest = data[0]
        for x in range(len(data)):
            if data[x] < lowest:
                lowest = data[x]
        sorted_data.append(lowest)
        data.remove(lowest)
    print(DF.loc[:, (sorted_data)] if choice == 'Column Name' else DF.loc[(sorted_data)])

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
grades.index = ['Test 1', 'Test 2', 'Test 3']
print(grades)

choice = input('\nSort by Row Name or Column Name: ')
if choice == 'Column Name':
    sort_function(grades, list(grades.keys()), choice)
elif choice == 'Row Name':
    sort_function(grades, list(grades.index), choice)