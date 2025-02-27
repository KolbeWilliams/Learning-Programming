#Exercise 4: Use np.linespace to creat a copy of the given graph
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 80)
plt.plot(x, np.sin(x), 'bo-',  label = 'sin(x)')
plt.plot(x, np.cos(x), 'r_-', label = 'cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend(loc = 'upper right')
plt.title('Trigonometric Functions: sin(x), cos(x)')
plt.show()
