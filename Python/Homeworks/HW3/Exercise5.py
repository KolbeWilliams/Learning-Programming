#Exercise 5: Use the filter() function and a lambda expression to print uppercase characters from a string
str1 = 'Computer Science'
result = (list(filter(lambda x: x if(ord(x) >= 65 and ord(x) <= 90) else(), str1)))
print(f'The capital letters in \"{str1}\" are: {result}')
