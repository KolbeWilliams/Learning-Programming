#Exercise 3: Write a function that finds the minimum with a varying number
#of arguments provided
def myMinimum(arg1 = 8, arg2 = 2, arg3 = 10):
    if(arg1 <= arg2 and arg1 <= arg3):
        return arg1
    elif(arg2 <= arg1 and arg2 <= arg3):
        return arg2
    else:
        return arg3

print(f'The smallest value is: {myMinimum()}')
print(f'The smallest value is: {myMinimum(7)}')
print(f'The smallest value is: {myMinimum(7, 1)}')
print(f'The smallest value is: {myMinimum(7, 1, -3)}')