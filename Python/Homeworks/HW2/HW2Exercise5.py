#Exercise 5: Write a function to reverse a list
def myReverse(li1):
    reverse = []
    for x in range(len(li1)):
        reverse.insert(x,li1[-1])
        li1.pop()
    return reverse

li = [0, 4, 9, 4, 8, 'world', 15, 4, 'Hello', -0.9]
print('The starting list is: ', end = '')
for x in range(len(li) - 1):
    print(f'{li[x]},', end = ' ')
print(li[len(li) - 1])
print()

li = myReverse(li)
print('The reversed list is: ', end = '')
for x in range(len(li) - 1):
    print(f'{li[x]},', end = ' ')
print(li[len(li) - 1])
print()