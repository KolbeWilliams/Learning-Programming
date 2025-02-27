#Exercise 4:
import pandas as pd
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

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90], 'Sam': [94, 77, 90], 'Katie': [100, 81, 82], 'Bob': [83, 65, 85]}
grades = pd.DataFrame(grades_dict)
grades.index = ['Test 1', 'Test 2', 'Test 3']
print(grades)

arr_wally = np.array(grades['Wally'])
arr_eva = np.array(grades['Eva'])
arr_sam = np.array(grades['Sam'])
arr_kaite = np.array(grades['Katie'])
arr_bob = np.array(grades['Bob'])
li = [arr_wally, arr_eva, arr_sam, arr_kaite, arr_bob]

keys = list(grades.keys())
print('\n20th percentile using built in function:')
for x in range(len(li)):
    print(f'{keys[x]}: {np.percentile(li[x], 20)}')

print('\n20th percentile without using built in function:')
for x in range(len(li)):
    print(f'{keys[x]}: {percentile_function(li[x], 20)}')

print('\n40th percentile using built in function:')
for x in range(len(li)):
    print(f'{keys[x]}: {np.percentile(li[x], 40)}')

print('\n40th percentile without using built in function:')
for x in range(len(li)):
    print(f'{keys[x]}: {percentile_function(li[x], 40)}')

print('\n60th percentile using built in function:')
for x in range(len(li)):
    print(f'{keys[x]}: {np.percentile(li[x], 60)}')

print('\n60th percentile without using built in function:')
for x in range(len(li)):
    print(f'{keys[x]}: {percentile_function(li[x], 60)}')

print('\n80th percentile using built in function:')
for x in range(len(li)):
    print(f'{keys[x]}: {np.percentile(li[x], 80)}')

print('\n80th percentile without using built in function:')
for x in range(len(li)):
    print(f'{keys[x]}: {percentile_function(li[x], 80)}')

