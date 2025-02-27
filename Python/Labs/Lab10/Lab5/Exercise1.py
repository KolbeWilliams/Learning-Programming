#Exercise 1: Use map and lambda to add elements of 2 tuples
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
print(list(map(lambda x, y: x + y, tpl1, tpl2)))
