#Exercsie 1: Create a lambda expression that computes the square root of a number
num = float(input("Enter a number: "))
result = lambda x : x ** 0.5
print(f'The square root of {num} is {result(num)}')
