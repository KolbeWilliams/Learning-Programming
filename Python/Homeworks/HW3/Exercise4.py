#Exercise 4: Convert a string to words
def str2words(myStr):
    li = []
    temp = ''
    for x in range(len(myStr)):
        if(myStr[x] != ' '):
            temp += myStr[x]
        elif(myStr[x] == ' '):
            if(temp != ''):
                li.append(temp)
            temp = ''
    if(temp != ''):
        li.append(temp)
    return li

myStr = input('Enter a string: ')
words = str2words(myStr)
print('List of words:', words)
