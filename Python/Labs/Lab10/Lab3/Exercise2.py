#Exercise 2: Print a list with user provided indicies
li = [9, 3, 0, -4, 8, 7, 10, -1, 5]
start = int(input('Enter a starting index:'))
stop = int(input('Enter an ending index (will go to 1 less than index entered):'))
step = int(input('Enter a step for the printed list:'))
print(li[start:stop:step])
