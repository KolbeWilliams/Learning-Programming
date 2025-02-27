#Exercise 2: Create a 3D numpy array and ask user enter float values into it and to modify an element
import numpy as np
arr = np.zeros((3, 2, 2))
for d in range(3):
    for r in range(2):
        for c in range(2):
            num = float(input('Enter a floating point number:'))
            arr[d, r, c] = num
print(f'The array is: \n{arr}')
index1 = int(input('Provide the first index of the value you mant to modify: '))
index2 = int(input('Provide the second index of the value you mant to modify: '))
index3 = int(input('Provide the third index of the value you mant to modify: '))
newValue = float(input('Enter the new value of that index: '))
arr[index1, index2, index3] = newValue
print(f'The new array is: \n{arr}')
