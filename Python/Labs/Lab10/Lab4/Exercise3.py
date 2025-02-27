#Exercise 3: Use a lambda function and the filter() function to filter out lowercase characters
str1 = 'Computer Science'
print('The uppercase characters in the string are:', list(filter(lambda x: ord(x) >= 65 and ord(x) <= 90, str1)))