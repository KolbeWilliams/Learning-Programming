#Exercise 2:
import numpy as np
import matplotlib.pyplot as plt

x = np.array([-5, -1, 3, 7, 5, 9])
y = np.array([-10, -3, 5, 8, 7, 9])
plt.scatter(x,y)

w1 = ((np.mean(x * y)) - (np.mean(x) * np.mean(y))) / ((np.mean(x ** 2)) - (np.mean(x) ** 2))
w0 = np.mean(y) - (w1 * np.mean(x))
model = w1 * x + w0

plt.plot(x, model, label = f'y = {w1:.1f}x+{w0:.1f}', color = 'g')
plt.title('Ordinary Least Squares Regression Line: y = mx + b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
