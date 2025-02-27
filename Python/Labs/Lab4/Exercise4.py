#Exercise 4: Print a name and greeting given as inputs using a lambda function
def greetingFunction(name, greeting):
    print(f'{greeting} {name}')

name = input('Enter a name: ')
greeting = input('Enter a greeting: ')
output = lambda name, greeting: print(f'{greeting} {name}')
output(name,greeting)
