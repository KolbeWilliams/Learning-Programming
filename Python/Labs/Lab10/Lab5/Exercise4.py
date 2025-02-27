#Exercise 4: Sum the integers in a list in one line using lambda, filter, and reduce
from functools import reduce
li = [10, 'Hi', 20, 'Hello', 30, 'World', 40]
print('The sum is:', reduce(lambda x, y: x + y, filter(lambda x: type(x) == int, li)))
