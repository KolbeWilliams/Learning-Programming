#Exercise 3: Use sympy is find the derivative of the equation f(x) = 3x^2 - 3x + 4
#Print the function and the differentiated one. Compute for which value of x the differentiated
#function becomes 0 using sp.solve(). Plot the function, the differentiated one, and (in red) the point at which the
#derivative becomes 0.
import sympy as sp
from matplotlib import pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline #I did NOT us AI for this, I looked into other libraries to make a less rigid graph

#Differentiate and solve
x = sp.symbols('x')
f = (3*(x**2) - 3*x + 4)
f_prime = sp.diff(f, x)
print('f(x) =', f)
print("f'(x) =", f_prime)
zero_point = sp.solve(f_prime, x)
print("f'(x) = 0 when x =", zero_point)

#Plot f(x) and f'(x)
f_plot = sp.lambdify(x, f)
fPrime_plot = sp.lambdify(x, f_prime)
x_values = np.arange(-2,4,1)
y_values = f_plot(x_values)
yPrime_values = fPrime_plot(x_values)

#Make f(x) appear smooth (again I resaerched other libraries and did NOT use AI)
smooth_line = make_interp_spline(x_values, y_values) #Uses the given data points to estimate the coefficients for the spline curve
X = np.linspace(x_values.min(), x_values.max()) #Retruns evenly spaced numbers over the specified interval
Y = smooth_line(X) #Finds the y-values for the evenly spaced x-values

plt.plot(X, Y, label = 'f(x)', color = 'b')
plt.plot(x_values, yPrime_values, label = "f'(x)", color = 'tab:orange')
plt.grid(True, color = 'k')
plt.legend()

#Plot point where f'(x) = 0
plt.scatter(zero_point, 0, color = 'r')
plt.show()


