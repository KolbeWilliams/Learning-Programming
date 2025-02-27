#Exercise 2: Write a function to find characters within a given string
def myFind(string, character):
    count = 0
    indicies = []
    print('The index/indicies of your character within your string are: ', end = '')
    for x in range(len(string)):
        if(string[x] == character):
            indicies.append(x)
            count += 1
    for x in range(len(indicies) - 1):
            print(f'{indicies[x]},', end = ' ')
    print(indicies[len(indicies) - 1])
    return count

myStr = input('Enter a string: ')
char = input('Enter a single character: ')
print(f'\nThe number of times your character appears in your string is: {myFind(myStr, char)}')

