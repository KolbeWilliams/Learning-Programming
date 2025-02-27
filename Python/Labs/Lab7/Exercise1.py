#Exercsie 1: Create a numpy array from -1 to +1.1 with a step of 0.1 Then plot inverse sine
#Add title, xlabel, ylabel 
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-1, 1.1, .1)
y = np.degrees(np.arcsin(x))
plt.plot(x, y)
plt.title('Plot of $sin^{-1}$')
plt.xlabel('Sine')
plt.ylabel('Angle (degrees)')
plt.show()