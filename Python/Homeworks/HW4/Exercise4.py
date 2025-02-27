#Exercise 4: Create a function and use the filter() function to filter out data types that are not integers from a list
def int_dataTypes(x):
    return type(x) == int

li = [9, "Robot", 3.14, 8, "Vision"]
print(f'The list with only integers is: {list(filter(int_dataTypes,li))}')