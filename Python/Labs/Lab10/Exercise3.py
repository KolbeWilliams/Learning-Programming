#Exercise 3:
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
b1 = A[0]
m1 = A[1]
line = np.array([x for x in b1 + m1 * np.array(x)])
b2 = 0.5
m2 = 1.0
b3 = 0.0
m3 = 1.2
line2 = np.array([x for x in b2 + m2 * np.array(x)])
line3 = np.array([x for x in b3 + m3 * np.array(x)])
sse1 = []

sse1 = np.sum((y - line) ** 2)
print(f'The Sum of Squared Errors for the regression line is: {sse1:.2f}')
sse2 = np.sum((y - line2) ** 2)
print(f'The Sum of Squared Errors for the y = 0.5 + x line is: {sse2:.2f}')
sse3 = np.sum((y - line3) ** 2)
print(f'The Sum of Squared Errors for the y = 1.2x line is: {sse3:.2f}')

plt.scatter(x,y)
plt.plot(x, line, label = f'y = {m1:.1f}x{b1:.1f}', color = 'g')
plt.plot(x, line2, label = f'y = {m2}x+{b2}', color = 'r')
plt.plot(x, line3, label = f'y = {m3}x+{b3}', color = 'b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Least Squares Regression Line: y = mx + b')
plt.legend()
plt.show()
