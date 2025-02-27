#Exercise 1: Create 2 different sets and ask the user what tasks they want to perform on the sets. Then write functions to perform the tasks.
def add(subject):
    num = int(input('What number do you wish to add: '))
    subject.add(num)
    
def remove(subject):
    num = int(input('What number do you wish to remove: '))
    subject.remove(num)
    
def union(subject1, subject2):
    result = subject1.union(subject2)
    return result
    
def intersection(subject1, subject2):
    result = subject1.intersection(subject2)
    return result
    
def difference(subject1, subject2):
    result = subject1.difference(subject2)
    return result
    
def symmetricDifference(subject1, subject2):
    result = subject1.symmetric_difference(subject2)
    return result
    
def disjoint(subject1, subject2):
    if(subject1.isdisjoint(subject2) == True):
        return 'There are no elements in common'
    else:
        return 'The two sets have elements in common'

li = [x for x in range(10,21)]
set_A = {x for x in li}
set_B = {x for x in li[1: :2]}
print('Set A:', set_A)
print('Set B:', set_B)
end = 0
while(end == 0):
    choice = input('Do you want to "add", "remove", "union", "intersection", "difference", "symmetric difference", or "disjoint" the sets or "EXIT" the program: ')
    if(choice == 'add'):
        modification = input('Do you wish to modify set "A" or set "B": ')
        if(modification == 'A'):
            argument = set_A
        elif(modification == 'B'):
            argument = set_B
        add(argument)
        print(f'Adding this number to set {modification} results in: {argument}')
    elif(choice == 'remove'):
        modification = input('Do you wish to modify set "A" or set "B": ')
        if(modification == 'A'):
            argument = set_A
        elif(modification == 'B'):
            argument = set_B
        remove(argument)
        print(f'Removing this number from {modification} results in: {argument}')
    elif(choice == 'union'):
        print(f'Unioning the sets results in: {union(set_A, set_B)}')
    elif(choice == 'intersection'):
        result = intersection(set_A, set_B)
        print(f'Intersecting the sets results in: {result}')
    elif(choice == 'difference'):
        result = difference(set_A, set_B)
        print(f'Taking the difference of the sets results in: {result}')
    elif(choice == 'symmetric difference'):
        result = symmetricDifference(set_A, set_B)
        print(f'Taking the symmetric difference of the sets results in: {result}')
    elif(choice == 'disjoint'):
        result = disjoint(set_A, set_B)
        print(f'Disjointing the sets results in: {result}')
    elif(choice == 'EXIT'):
        end += 1
    else:
        print('Please enter a valid input')