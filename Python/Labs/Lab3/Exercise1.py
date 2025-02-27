#Exercise 1: Conver string to uppercase using a function
def myToUpper(myStr):
    newStr = ''
    for x in range (len(myStr)):
        if(ord(myStr[x]) >= 97 and ord(myStr[x]) <= 122):
            newStr += (chr(ord(myStr[x]) - 32))
        else:
            newStr += (myStr[x])
    return newStr

myStr = input("Enter a string:")
myStr = myToUpper(myStr)
print(f'Uppercase String: {myStr}')