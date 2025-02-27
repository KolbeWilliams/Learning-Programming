#Exercise 4:
import numpy as np
from scipy import stats

x = np.array([-5, -1, 3, 7, 5, 9])
y = np.array([-10, -3, 5, 8, 7, 9])

slope, intercept, r, p, std_err = stats.linregress(x,y)
model = slope * x + intercept
sst = np.sum((y - np.mean(y)) ** 2)
print(f'SST: {sst}')
ssr = np.sum((model - np.mean(y)) ** 2)
print(f'SSR: {ssr}')
sse = np.sum((model - y) ** 2)
print(f'SSE: {sse}')
r_squared = 1 - (sse / sst)
r = r_squared ** (1/2)
print(f'r: {r}')
print(f'R^2: {r_squared}')