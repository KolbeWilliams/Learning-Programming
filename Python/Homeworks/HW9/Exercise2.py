#Exercise 2:
import matplotlib.pyplot as plt
import numpy as np

square_feet = np.array([250., 500, 1000, 2000, 3000, 4000])
prices = np.array([50000., 100000, 200000, 400000, 600000, 800000])

#Create noise
noise = np.random.normal(0.0, 1.0, len(prices)) * 30000
prices_noise = prices + noise

#Regression Line without noise exercise 1
w1 = ((np.mean(square_feet * prices)) - (np.mean(square_feet) * np.mean(prices))) / ((np.mean(square_feet ** 2)) - (np.mean(square_feet) ** 2))
w0 = np.mean(prices) - (w1 * np.mean(square_feet))
model_ex1 = w1 * square_feet + w0
#Regression Line without noise exercise 2
x = square_feet.reshape(-1, 1)
y = prices
ones = np.ones((len(x), 1))
x = np.hstack((ones, x))
A = np.linalg.inv(x.T @ x) @ (x.T @ y)
model = A[1] * square_feet + A[0]
print(f'Slope in exercise 1: {w1:.2f}\nSlope in exercise 2: {A[1]:.2f}')
print(f'Intercept in exercise 1: {w0:.2f}\nIntercept in exercise 2: {A[0]:.2f}')

#Regression Line with noise exercise 1
w1_noise = ((np.mean(square_feet * prices_noise)) - (np.mean(square_feet) * np.mean(prices_noise))) / ((np.mean(square_feet ** 2)) - (np.mean(square_feet) ** 2))
w0_noise = np.mean(prices_noise) - (w1_noise * np.mean(square_feet))
model_noise_ex1 = w1_noise * square_feet + w0_noise
#Regression Line with noise exercise 2
y = prices_noise
A_noise = np.linalg.inv(x.T @ x) @ (x.T @ y)
model_noise = A_noise[1] * square_feet + A_noise[0]
print(f'\nSlope with noise in exercise 1: {w1_noise:.2f}\nSlope with noise in exercise 2: {A_noise[1]:.2f}')
print(f'Intercept with noise in exercise 1: {w0_noise:.2f}\nIntercept with noise in exercise 2: {A_noise[0]:.2f}\n')

#Find SSE and r without noise
sse = 0
for x in range(len(prices)):
    sse += (model[x] - prices[x]) ** 2
sst = 0
for x in range (len(prices)):
    sst += (prices[x] - np.mean(prices)) ** 2
r_squared = 1 - (sse / sst)
r = r_squared ** (1/2)
print('SSE and r without noise:')
print(f'SSE: {sse}\nr: {r}')

#Find SSE and r with noise
sse_noise = 0
for x in range(len(prices_noise)):
    sse_noise += (model_noise[x] - prices_noise[x]) ** 2
sst_noise = 0
for x in range (len(prices_noise)):
    sst_noise += (prices_noise[x] - np.mean(prices_noise)) ** 2
r_squared_noise = 1 - (sse_noise / sst_noise)
r_noise = r_squared_noise ** (1/2)
print('\nSSE and r with noise:')
print(f'SSE: {sse_noise}\nr: {r_noise}')

new_square_feet = np.array([200, 1250, 2710, 5100])
#Precict New prices without noise
new_prices = A[1] * new_square_feet + A[0]
print('\nPredicted Prices without noise:')
for x in range(len(new_square_feet)):
    print(f'{new_square_feet[x]} square feet: ${new_prices[x]:.2f}')

#Predict new prices with noise
new_prices_noise = A_noise[1] * new_square_feet + A_noise[0]
print('\nPredicted Prices with noise:')
for x in range(len(new_square_feet)):
    print(f'{new_square_feet[x]} square feet: ${new_prices_noise[x]:.2f}')

plt.scatter(square_feet, prices, label = 'Before Noise', color = 'g')
plt.scatter(square_feet, prices_noise, label = 'After Noise', color = 'r')
plt.plot(square_feet, model, label = f'Regression Line before Noise', color = 'g')
plt.plot(square_feet, model_noise, label = f'Regression Line after Noise', color = 'r')
plt.title('Linear Regression with and without noise')
plt.legend()
plt.show()