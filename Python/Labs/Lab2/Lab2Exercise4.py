#Exercise 4: Ask user for a string and write a function to print the uppercase characters
#and return the number of uppercase charactrs
def upperCaseCharacters(str):
    count = 0
    print('Uppercase Characters: ', end = '')
    for x in range(len(str)):
        if(ord(str[x]) >= 65 and ord(str[x]) <= 90):
            print(str[x], end = '')
            count += 1
    print('\nNumber of Uppercase Characters: ', end = '')
    return count

myStr = input('Enter a string: ')
print(upperCaseCharacters(myStr))
