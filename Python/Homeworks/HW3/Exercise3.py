#Exercise 3: Filter out non-prime numbers from a list
def is_Prime(x):
    check = 0
    middle = int(x / 2)
    for i in range(2, middle):
        if((x / i).is_integer()):
            check += 1
    if(check == 0):
        return True
    else:
        return False

numbers = [23, 2, 9, 7, 14, 18, 3, 24, 16, 5, 8, 97]
result = list(filter(is_Prime,numbers))
print(f'The prime numbers in the list are: {result}')
