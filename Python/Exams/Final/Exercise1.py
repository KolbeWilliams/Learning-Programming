#Exercise 1:
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Ex1_dataset.csv', names = ['x', 'y'])
x = np.array(df['x'])
y = np.array(df['y'])

SSEs = []
for i in range(2,5):
    coefficients = np.polyfit(x, y, i)
    y_valuesTest = np.polyval(coefficients, x)
    sse = np.sum((y_valuesTest - y)**2)
    SSEs.append([y_valuesTest, sse])

smallest_error = np.inf
for i in range(len(SSEs)):
    if SSEs[i][1] < smallest_error:
        smallest_error = SSEs[i][1]
        index = i + 2

for i in range(2,5):
    print(f'The SSE of a polynomial with degree {i} is {SSEs[i - 2][1]}')
print(f'The ploynomial with the smallest error is a polynomial with degree {index} because it has the smallest SSE')
plt.scatter(x, y, label = 'data points')
plt.plot(x, SSEs[index - 2][0], label = 'best fit polynomial')
plt.ylabel('y-axis')
plt.xlabel('x-axis')
plt.title('Optimal Polynomial')
plt.legend()
plt.show()