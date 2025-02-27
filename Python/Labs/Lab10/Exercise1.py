#Exercise 1:
import numpy as np
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 2, 4, 4, 6]
x_matrix = np.array(x)
x_matrix.resize(len(x), 1)
ones = np.ones((len(x), 1))
x_matrix = np.hstack((ones, x_matrix))
y_matrix = np.array(y)
x_transposed = x_matrix.T
x_multiplied = x_transposed @ x_matrix
y_multiplied = x_transposed @ y_matrix
A = np.linalg.inv(x_multiplied)
A = A @ y_multiplied
b = A[0]
m = A[1]
line = np.array([x for x in b + m * np.array(x)])


plt.scatter(x,y)
plt.plot(x, line, label = f'y = {m:.1f}x{b:.1f}', color = 'g')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Least Squares Regression Line: y = mx + b')
plt.legend()
plt.show()
