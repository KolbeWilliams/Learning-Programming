#Exercise 4: Convert a string to a list and then convert characters to uppercase

def myToUpper(li):
    new = []
    for x in range(len(li)):
        if(ord(li[x]) >= 97 and ord(li[x]) <= 122):
            new.append(chr(ord(li[x]) - 32))
        else:
            new.append(li[x])
    return new

myStr = input('Enter a string: ')
print(f'\nList before: ', end = '')
for x in range (len(myStr)):
    print(myStr[x], end = '')

list(myStr)
print(f'\nList after:  ', end = '')
myStr = myToUpper(myStr)
for x in range (len(myStr)):
    print(myStr[x], end = '')
print()
