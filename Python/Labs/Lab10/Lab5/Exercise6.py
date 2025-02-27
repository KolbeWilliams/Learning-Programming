#Exercise 6: Use map, lambda, and filter to print the strings in a list in uppercase in one line
li = [10, 'Hi', 20, 'Hello', 30, 'World', 40]
print(list(map(lambda x: x.upper(), filter(lambda x: type(x) == str, li))))
