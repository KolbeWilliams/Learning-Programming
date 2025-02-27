#Exercise 1: Use Newton's method to calculate the square root of a number provided by the user
from decimal import *
getcontext().prec = 50 #sets decimal precision to 50 paces so all of the outputs are fully visible
threshold = 1e-8 #given threshold
num = int(input('Enter a positive integer: '))
guess = float(input('Enter a guess for the square root: '))
ans = [0, guess] #stores calculated values in the list to use in the while loop
count = 1
while(abs(Decimal(ans[-1]) - Decimal(ans[-2])) > threshold): #checks the difference between the last 2 iterations
    print(f'Iteration {count}: ', end = '')
    ans.append(Decimal((ans[-1] + num / ans[-1]) / 2))
    print(ans[-1])
    count += 1
print(f'The square root of {num} is approxiamently: {round(ans[-1],8)}')
