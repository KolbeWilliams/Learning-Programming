#Exercise 2: Use a lambda function to do distance converstions based on a choice by the user
choice = 0
while(choice != 1 and choice != 2):
    choice = int(input('Enter "1" for Miles->Kilometers or "2" for Kilometers->Miles: '))
    if(choice != 1 and choice != 2):
        print('Invalid input, please enter either "1" or "2"')
distance = float(input('Enter a distance: '))
conversion = lambda choice, distance: (f'{distance} miles is equal to {distance * 1.609} kilometers' if(choice == 1) 
                else(f'{distance} kilometers is equal to {distance / 1.609} miles'))
print(conversion(choice, distance))
