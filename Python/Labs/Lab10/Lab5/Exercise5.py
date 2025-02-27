#Exercise 5: Find minimum integer of a list reduce, lambda, and filter in one line
from functools import reduce
li = [10, 'Hi', 20, 'Hello', 30, 'world', 40]
print('The minimum number is:', reduce(lambda x, y: x if x < y else y, filter(lambda x: type(x) == int, li)))
