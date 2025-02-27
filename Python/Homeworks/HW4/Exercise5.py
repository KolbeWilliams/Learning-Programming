#Exercise 5: Use the filter() function and a lambda function to filter out data types that are not strings from a list
li = [9, "Robot", 3.14, 8, "Vision"]
print(f'The list with only strings is: {list(filter(lambda x: type(x) == str,li))}')