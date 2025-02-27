#Exercise 1: import functions to add, subtract, multiply, and divide two 
#float numbers provided by the user
from myFunctions import add, subtract, multiply, divide

num1 = float(input("Enter a float number: "))
num2 = float(input("Enter another float number: "))

while(True):
    choice = input('Enter "+" to add, "-" to subtract, "*" to multiply, or "/" to divide: ')
    if(choice == '+'):
        print(f'{num1} + {num2} is {add(num1, num2)}')
    elif(choice == '-'):
        print(f'{num1} - {num2} is {subtract(num1, num2)}')
    elif(choice == '*'):
        print(f'{num1} * {num2} is {multiply(num1, num2)}')
    elif(choice == '/'):
        print(f'{num1} / {num2} is {divide(num1, num2)}')
    else:
        print('Please enter a valid operation')