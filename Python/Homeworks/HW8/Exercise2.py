#Exercise 2:
import pandas as pd
from functools import reduce
import numpy as np
import math

def percentile_function(arr, percentile):
    arr.sort()
    index = (len(arr) - 1) * percentile / 100
    if type(index) == int:
        return arr[index]
    else:
        lower = math.floor(index)
        upper = lower + 1
        return arr[lower] + (index - lower) * (arr[upper] - arr[lower])

def describe_function(DF):
    keys = (list(DF.keys()))
    print('\t', end = '')
    for x in range(len(keys)):
        print(keys[x], '\t', end = '')
    print('\ncount\t', end = '')
    for x in range(len(keys)):
        count = float(len(DF.iloc[:, x]))
        print(f'{count:.2f}', '\t', end = '')
    print('\nmean\t', end = '')
    for i in range(len(keys)):
        mean = reduce(lambda x, y: x + y, DF.iloc[:, i]) / len(DF.iloc[:, i])
        print(f'{mean:.2f}\t', end = '')
    print('\nstd\t', end = '')
    for i in range(len(keys)):
        summation = 0
        count = float(len(DF.iloc[:, i]))
        mean = reduce(lambda x, y: x + y, DF.iloc[:, i]) / len(DF.iloc[:, i])
        for x in range(len(DF.iloc[:, i])):
            summation += (DF.iloc[x, i] - mean) ** 2
        std = (1 / (count - 1) * summation) ** 0.5
        print(f'{std:.2f}\t', end = '')
    print('\nmin\t', end = '')
    for i in range(len(keys)):
        minimum = reduce(lambda x, y: x if x < y else y, DF.iloc[:, i])
        print(f'{minimum:.2f}\t', end = '')
    print('\n25%\t', end = '')
    for x in range(len(keys)):
        arr = np.array(DF.iloc[:, x])
        percent_25 = np.percentile(arr, 25)
        print(f'{percent_25:.2f}\t', end = '')
    print('\n50%\t', end = '')
    for x in range(len(keys)):
        arr = np.array(DF.iloc[:, x])
        arr.sort()
        percent_50 = percentile_function(arr, 50)
        print(f'{percent_50:.2f}\t', end = '')
    print('\n75%\t', end = '')
    for x in range(len(keys)):
        arr = np.array(DF.iloc[:, x])
        percent_75 = np.percentile(arr, 75)
        print(f'{percent_75:.2f}\t', end = '')
    print('\nmax\t', end = '')
    for i in range(len(keys)):
        maximum = reduce(lambda x, y: x if x > y else y, DF.iloc[:, i])
        print(f'{maximum:.2f}\t', end = '')
    print()

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
grades.index = ['Test 1', 'Test 2', 'Test 3']
pd.set_option('display.precision', 2)
print('Using built in function:\n', grades.describe())

print('\nWithout using built in function:')
describe_function(grades)