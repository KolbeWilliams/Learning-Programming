#Exercise 2: Ask user to enter min, max, and step values for x-axis and use np.arange() to create x array.
#Use eval() for y array and also include label, xlabel, ylabel, title, and legend
import numpy as np
from matplotlib import pyplot as plt

#Set up x-axis and y-axis
minimum = int(input('Enter the minimum value for the x-asis: '))
maximum = int(input('Enter the maximum value for the x-asis: '))
step = int(input('Enter the step for the x-asis: '))
x = np.arange(minimum, maximum, step, dtype = int)
expression = input('Enter an expression: ')
y = eval(expression)

#Create graph
plt.plot(x,y, label = 'x')
plt.title(f'Graph of {expression}')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()

