#Exercise 3:
import numpy as np
import matplotlib.pyplot as plt

def predictions(coefficients, exponents, x):
    num = 0
    for i in range(len(exponents)):
        num += coefficients[i] * x ** exponents[i]
    return num

x = np.array([-2, -1, 0, 1, 2])
y = np.array([3, 5, 1, 4, 10])

A = np.zeros((len(x), len(x)))
B = y
for i in range(len(x)):
    for j in range(len(x)):
        A[i][j] = x[i] ** j
coefficients = np.matmul(np.linalg.inv(A), B)
print('Coefficients:', [f'{i:.5f}' for i in coefficients])
exponents = np.array([i for i in range(len(coefficients))])
testing_points = np.arange(-3, 3, 0.1)
model = np.array(())
for i in range(len(testing_points)):
    model = np.append(model, predictions(coefficients, exponents, testing_points[i]))

plt.scatter(x, y, label = 'training points', color = 'r')
plt.plot(testing_points, model, label = 'testing points', color = 'blue', marker = '*')
plt.title('Polynomial Curve Fitting')
plt.xlabel('x-axis')
plt.ylabel('y-asis')
plt.ylim(-2, 12)
plt.legend()
plt.show()