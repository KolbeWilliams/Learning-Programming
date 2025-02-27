#Exercise 2: Create a Numpy array with 120 elements and values that range from ?1 to +10. Plot the
#tangent trigonometric function using the np.tan() built-in function.
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-1, 10, 120)
y = np.tan(x)
plt.plot(x, y)
plt.show()

