#Exercise 1: Create a 2x4 numpy array filled with zeros, use nested for loop to enter int values into the array,
#change the shape of the array to 4x2,and create two more arrays that consist of the numbers in the first and second
#columns from the original reshaped array.
import numpy as np

arr = np.zeros((2, 4), dtype = int)
print('Array with zeros:')
print(arr, '\n')

for row in range(len(arr)):
    for column in range(len(arr[0])):
        arr[row][column] = int(input('Enter a grade: '))

print('Array with values:')
print(arr, '\n')

arr = arr.reshape(4, 2)
print('Reshaped array:')
print(arr, '\n')

firstCol = arr[:, :1].flatten()
print('First column array:')
print(firstCol)
secondCol = arr[:, 1:].flatten()
print('\nSecond column array:')
print(secondCol, '\n')