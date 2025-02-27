#Exercise 3: Use a lambda function to do temperature converstions based on a choice by the user
choice = 0
while(choice != 1 and choice != 2):
    choice = int(input('Enter "1" for Fahrenheit->Celsius or "2" for Celsius->Fahrenheit: '))
    if(choice != 1 and choice != 2):
        print('Invalid input, please enter either "1" or "2"')
temperature = float(input('Enter a temperature: '))
conversion = lambda choice, temperature: (f'{temperature} degrees Fahrenheit is equal to {(temperature - 32) * (5/9)} degrees Celsius' 
                if(choice == 1) else(f'{temperature} degrees Celsius is equal to {temperature * (9/5) + 32} degrees Fahrenheit'))
print(conversion(choice, temperature))
