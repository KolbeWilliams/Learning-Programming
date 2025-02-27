#Exercise 5:
from matplotlib import colormaps
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 4, 4, 6])

slopes = intercepts = np.arange(-4, 4, 0.1)
X, Y = np.meshgrid(slopes, intercepts) #Create Slope and Intercept arrays
Z = np.zeros(X.shape) #Initialize SSE array
for i in range(X.shape[0]): #Iterate through slopes
    for j in range(X.shape[1]): #Interate through intercepts
        model = X[i, j] * x + Y[i, j] #Create a model foe each slope, intercept pair
        sse = np.sum((model - y) ** 2) #Calculate SSE for each model
        Z[i, j] = sse #add each SSE to the SSE array
smallest_error = 1000000
for i in range(len(Z[0])):
    for j in range(len(Z[1])):
        if Z[i][j] < smallest_error:
            smallest_error = Z[i][j]
            best_slope = X[i][j]
            best_intercept = Y[i][j]
best_model = best_slope * x + best_intercept

fig = plt.figure() #Creates a figure for the 3D subplot
ax = fig.add_subplot(111, projection=  '3d') #Create a 3D subplot
surf = ax.plot_surface(X, Y, Z, alpha = 0.75, cmap = 'Blues') #Plot the graph
fig.colorbar(surf, shrink = 0.99, aspect = 20)
ax.scatter(best_slope, best_intercept, smallest_error, label = f'SSE = {smallest_error}\nŷ={best_slope:.2f}{best_intercept:.2f}', color = 'r')
ax.set_title('3D surface plot of SSE as a function of m and b')
ax.set_xlabel('X axis (slope)')
ax.set_ylabel('Y axis (y-Intercept)')
plt.legend()
plt.show()