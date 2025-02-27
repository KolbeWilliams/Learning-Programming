#Exercise 7: Create a telephone dictionary and allow the user to perform different
#operations in the dictionary
def add(myDictionary):
    key = input('Enter the name of the person you want to add: ')
    value = input('Enter the number for the person you want to add: ')
    myDictionary[key] =  value
    print()

def remove(myDictionary):
    key = input('Enter the name of the person you want to remove: ')
    del myDictionary[key]
    print()

def search(myDictionary):
    key = input('Enter the name of the person whose number you are looking for: ')
    print(f"{key}'s phone number is: {myDictionary[key]}\n")

def printDictionary(myDictionary):
    for key, value in myDictionary.items():
        print(f'{key} {value}')
    print()

telephone = {'Johnny': '111-111'}
finish = True
while (finish):
    choice = input('Enter "add", "remove", "look for a number", "print", or "EXIT"'+
   ' to perform an operation on the telephone dictionary: ')
    if(choice == 'add'):
        add(telephone)
    elif(choice == 'remove'):
        remove(telephone)
    elif(choice == 'look for a number'):
        search(telephone)
    elif(choice == 'print'):
        printDictionary(telephone)
    elif(choice == 'EXIT'):
        printDictionary(telephone)
        finish = False
    else:
        print('Invalid input')