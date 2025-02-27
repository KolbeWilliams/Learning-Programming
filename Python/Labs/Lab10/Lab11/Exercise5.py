#Exercise 5:
import numpy as np
from pandas.tseries.offsets import Hour
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
#from sklearn.linear_model import LinearRegression

data = pd.read_csv('grades.csv', names = ['Hours Studied', 'Grades'])
print(data)
hours_studied = np.array(data.iloc[:, 0])
grades = np.array(data.iloc[:, 1])

slope, intercept, r, p, std_err = stats.linregress(hours_studied,grades)
model = slope * hours_studied + intercept
print(f'Slope: {slope}, y-intercept: {intercept}, r (correlation coefficient): {r},' + 
       f' p-value: {p}, Standard Error: {std_err}')
#model_2 = LinearRegression()
#x = hours_studied.reshape(-1, 1)
#coefficients = model_2.fit(x, grades)
#X_test = np.array(10.5).reshape(-1, 1)
#y_pred = model_2.predict(X_test)
y_pred = slope * 10.5 + intercept

plt.scatter(hours_studied, grades)
plt.scatter(10.5, y_pred, label = f'x = 10.5, ŷ = {y_pred:.2f}', color = 'orange')
plt.plot(hours_studied, model, label = f'y = {slope:.1f}x+{intercept:.1f}', color = 'g')
plt.title('Least Squares Regression Line: y = mx + b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid()
plt.legend()
plt.show()