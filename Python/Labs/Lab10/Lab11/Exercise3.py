#Exercise 3:
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([-5, -1, 3, 7, 5, 9])
y = np.array([-10, -3, 5, 8, 7, 9])
plt.scatter(x,y)

slope, intercept,r, p, std_err = stats.linregress(x,y)
print(f'Slope: {slope}, y-intercept: {intercept}, r (correlation coefficient): {r},' + 
       f' p-value: {p}, Standard Error: {std_err}')
model = slope * x + intercept
plt.plot(x, model, label = f'y = {slope:.1f}x+{intercept:.1f}', color = 'g')
plt.title('linregress() method Regression Line: y = mx + b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()


