#Exercise 2: Find the integers in a list and multiply them by two in one line using map, filter, and lambda
li = [10, 'Hi', 20, 'Hello', 30, 'World', 40]
print(list(map(lambda x: x * 2, filter(lambda x: type(x) == int, li))))