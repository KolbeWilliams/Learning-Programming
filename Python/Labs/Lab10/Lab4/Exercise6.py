#Exercise 6: Search for a name in a dictionary given by user input and print information if found
catalog = {'Johnny' : [120, 3.5], 'Mary' : [71, 3.73], 'Jimmy' : [15, 2.9], 'Crystal' : ['103', 3.15]}
name = input('Enter name: ')
keys = list(catalog.keys())
found = 0
for i in range(len(keys)):
    if(keys[i] == name):
        print(f'\nName: {name}\nCredits: {catalog[name][0]}\nGPA: {catalog[name][1]}')
        found += 1
if(found == 0):
    print(f'{name} Not Found')