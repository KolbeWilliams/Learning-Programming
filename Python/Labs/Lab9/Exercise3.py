#Exercise 3:
import os
import getpass

with open('password.txt', 'w') as file:
    file.write('myCryptoPassword')
file.close()

chances = 3
with open('password.txt', 'r') as file:
    contents = file.read()
while chances != 0:
    passwd = getpass.getpass('Enter password: ')
    if passwd != contents and chances == 1:
        os.system('shutdown -s')
        chances = 0
    elif passwd != contents:
        chances -= 1
        print(f'Incorrect, you have {chances} more tries!')
    else:
        print('Correct password entered')
        chances = 0