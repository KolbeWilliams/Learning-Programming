#Exercise 2: Find min, max, mean, and standard deviation of first and second semester in different ways
import numpy as np

arr = np.zeros((2, 4), dtype = int)
for row in range(len(arr)):
    for column in range(len(arr[0])):
        arr[row][column] = int(input('Enter a grade: '))
print(f'Array: \n{arr}\n')
#minimum of first semester
minimum1 = arr[0][0]
for x in arr[0, :]:
    if (x <= minimum1):
        minimum1 = x
print('The minimum of the first semseter is:', minimum1)
#minimum of second semester
minimum2 = arr[1][0]
for x in arr[1, :]:
    if (x <= minimum2):
        minimum2 = x
print('The minimum of the second semseter is:', minimum2)
#Maximum of the first semester
maximum1 = arr[0][0]
for x in arr[0, :]:
    if (x >= maximum1):
        maximum1 = x
print('The maximum of the first semseter is:', maximum1)
#Maximum of the second semester
maximum2 = arr[1][0]
for x in arr[1, :]:
    if (x >= maximum2):
        maximum2 = x
print('The maximum of the second semseter is:', maximum2)
#Mean of the first semester
mean1 = 0
for x in arr[0, :]:
    mean1 += x
mean1 /= len(arr[0])
print('The mean of the first semseter is:', mean1)
print(f'Mean using mean() function: {np.mean(arr[0])}')
#Mean of the second semester
mean2 = 0
for x in arr[1, :]:
    mean2 += x
mean2 /= len(arr[1])
print('The mean of the second semseter is:', mean2)
print(f'Mean using mean() function: {np.mean(arr[1])}')
#Standard deviation of the first semester
n = len(arr[0])
xBar = mean1
sum = 0
for x in arr[0, :]:
    sum += (x - xBar) ** 2
std1 = ((1 / (n - 1)) * sum) ** .5
print('The standard deviation of the first semseter is:', std1)
print('Standard deviation using the std() function:', np.std(arr[0], ddof=1))
#Standard deviation of the second semester
n = len(arr[1])
xBar = mean2
sum = 0
for x in arr[1, :]:
    sum += (x - xBar) ** 2
std2 = ((1 / (n - 1)) * sum) ** .5
print('The standard deviation of the first semseter is:', std2)
print('Standard deviation using the std() function:', np.std(arr[1], ddof = 1))