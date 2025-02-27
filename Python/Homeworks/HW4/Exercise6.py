#Exercise 6: Convert the string element of a list to uppercase using only one line
myList = [3, 9.45, 'Robotics', 8, 1]
print("".join(list(map(lambda x: x if('A' <= x <= 'Z') else(chr(ord(x) - 32)),list(filter(lambda x: type(x) == str, myList))[0]))))