#Exercise 3: Create functions to replicate built-in count and index function for a tuple
def count(tpl, x):
    counter = 0
    for i in range (len(tpl)):
        if(tpl[i] == x):
            counter += 1
    return counter

def index(tpl, x):
    for i in range(len(tpl)):
        if(tpl[i] == x):
            return i
    return 'Value not found in tuple'

tu1 = (9, 3, 0, -4, 8, 7, 10, -1, 5)
#The value I used is 3, but any value could be passed to the functions
print(f'The value 3 is found in the tuple {count(tu1, 3)} time(s)')
print(f'The index of the first occurrance of 3 is: index {index(tu1, 3)}')