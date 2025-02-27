#Exercise 1: Create a function to find indecies of a number in a list
def myFind(li, x):
    listIndex = []
    for i in range(len(li)):
        if(li[i] == x):
            listIndex.append(i)
    return listIndex

numbers = [9, -3, 7, 2, 1, 2, 9, 9, 8, 2, 0, 0, 9, 2]
num = int(input('Enter a number: '))
print(f'The indicies of the number you entered in the list are: {myFind(numbers,num)}')
