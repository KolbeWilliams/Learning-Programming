#Exercise 3: Use a function to count the number of words in a given string

#extraSpace() function checks if there are extra spaces in between words
def extraSpace(string, index, count):
    if(string[index] != ' ' and count != 0):
        return False
    elif(string[index] == ' ' and index == 0 and string[index + 1] != ' '):
        return False
    elif(index == 0):
        return True
    elif(string[index + 1] == ' '):
        return True
    elif(string[index + 1] != ' '):
        return False

def countWords(string):
    count = 0
    if(string[0] != ' '):
        count += 1
    for x in range(len(string)):
        #This if statement checks for a space that is not the last character
        if(string[x] == ' ' and x != len(string) - 1 and extraSpace(string, x, count) == False):
            count += 1
    #This if statement is only used if there is one word with spaces in front of it
    if(count == 0):
        check = 0
        for x in range(len(string)):
            if(string[x] != ' '):
                check += 1
        if(check != 0):
            count += 1
    return count

myStr = input('Enter a string: ')
print(f'The number of words in your string is: {countWords(myStr)}')