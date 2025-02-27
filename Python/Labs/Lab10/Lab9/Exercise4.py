#Exercise 4:
from matplotlib import pyplot as plt
import pandas as pd

df = pd.read_csv('cars.csv', usecols = ['Car', 'Model', 'CO2'])
print(df)

ford_co2 = []
ford_models = []
mercedes_co2 = []
mercedes_models = []
for x in range(df.shape[0]):
    if df.iloc[x, 0] == 'Ford':
        ford_co2.append(df.iloc[x, 2])
        ford_models.append(df.iloc[x, 1])
    if df.iloc[x, 0] == 'Mercedes':
        mercedes_co2.append(df.iloc[x, 2])
        mercedes_models.append(df.iloc[x, 1])

ford_average = 0
for x in ford_co2:
    ford_average += x
ford_average /= len(ford_co2)
print(f'\nAverage CO2 emmisions for Ford: {ford_average}')

mercedes_average = 0
for x in mercedes_co2:
    mercedes_average += x
mercedes_average /= len(mercedes_co2)
print(f'Average CO2 emmisions for Mercedes: {mercedes_average}')

fig, ax = plt.subplots(nrows = 1, ncols = 2)
ax[0].plot(ford_models, ford_co2, 'b-o', label = 'Ford $CO_2$')
ax[0].scatter(ford_models, ford_co2, color = 'b')
ax[0].set_title('Ford $CO_2$ Emissions')
ax[0].set_xlabel('Model')
ax[0].set_ylabel('$CO_2$')
ax[0].axhline(y=ford_average, color='gray', linestyle='--', label='Average')
ax[0].set_ylim(50, 150)
ax[0].legend()

ax[1].plot(mercedes_models, mercedes_co2, 'r-o', label = 'Mercedes $CO_2$')
ax[1].scatter(mercedes_models, mercedes_co2, color = 'r')
ax[1].set_title('Mercedes $CO_2$ Emissions')
ax[1].set_xlabel('Model')
ax[1].set_ylabel('$CO_2$')
ax[1].axhline(y=mercedes_average, color='gray', linestyle='--', label='Average')
ax[1].set_ylim(50, 150)
ax[1].legend()
plt.show()
