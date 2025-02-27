#Exercise 4: Use the filter function to print only uppercase characters
def isUpper(x):
    return ord(x) >= 65 and ord(x) <= 90

str1 = 'Computer Science'
result = filter(isUpper,str1)
result = list(result)
print(f'Uppercase Characters: {result}')


