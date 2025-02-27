#Exercise 1:
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-5, -1, 3, 7, 5, 9])
y = np.array([-10, -3, 5, 8, 7, 9])
plt.scatter(x,y)

ones = np.ones((len(x), 1))
x.resize(len(x),1)
x = np.hstack((ones, x))
A = np.linalg.inv(x.T @ x) @ x.T @ y
intercept = A[0]
slope = A[1]
model = slope * x[:,1] + intercept
plt.plot(x[:,1], model, label = f'y = {slope:.1f}x+{intercept:.1f}', color = 'g')
plt.title('Least Squares Regression Line: y = mx + b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()