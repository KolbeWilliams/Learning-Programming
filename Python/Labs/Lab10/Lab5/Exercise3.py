#Exercise 3: Multiply integers in a list by 2 in 1 line using list comprehension
li = [10, 'Hi', 20, 'Hello', 30, 'World', 40]
print([x * 2 for x in li if (type(x) == int)])