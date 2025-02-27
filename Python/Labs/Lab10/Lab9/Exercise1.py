#Exercise 1:
import pandas as pd
from datetime import date
import csv

def mySplit(data):
    values = []
    string = ''
    num = ''
    end = ''
    for x in data:
        if (x < '0' or x > '9') and x != '.':
            string += x
        elif (x >= '0' and x <= '9') or x == '.':
            num += x
    values.append(string)
    values.append(float(num))
    return tuple(values)

df = pd.DataFrame(columns=['Product Name', 'Price'])
x = 0
while True:
    usr_input = input('Enter the product name and the price in one line or enter "-999" as the name or price to end: ')
    if '-999' in usr_input:
        break
    else:
        name, price = mySplit(usr_input)
        df.loc[x] = (name, price)
        x += 1
currentDate = date.today()
with open (f'myReceipt_{currentDate}.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    for x in range(df.shape[0]):
        writer.writerow(df.iloc[x])


