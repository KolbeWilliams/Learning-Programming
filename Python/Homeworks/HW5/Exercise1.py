#Exercise 1: Create plot, scatter, stack, and pie plots for the given lists
from matplotlib import pyplot as plt

fruitName = ['Apples', 'Oranges', 'Cherries', 'Watermelon']
fruitQuantity_2020 = [25, 25, 10, 18]
fruitQuantity_2021 = [22, 18, 9, 19]

fig, ax = plt.subplots(nrows = 2, ncols = 2)
#plot
ax[0][0].plot(fruitName, fruitQuantity_2020, label='2020', color = 'b')
ax[0][0].plot(fruitName, fruitQuantity_2021, label='2021', color = 'c')
ax[0][0].legend()

#scatter
ax[0][1].scatter(fruitName, fruitQuantity_2020, label='2020', color = 'b')
ax[0][1].scatter(fruitName, fruitQuantity_2021, label='2021', color = 'c')
ax[0][1].legend()

#stack
ax[1][0].stackplot(fruitName, fruitQuantity_2020, fruitQuantity_2021, colors = ['b', 'c'], labels = ['2020', '2021'])
ax[1][0].legend()

#pie
totalQuantity = []
for x in range(len(fruitQuantity_2020)):
    totalQuantity.append(fruitQuantity_2020[x] + fruitQuantity_2021[x])
ax[1][1].pie(totalQuantity, labels = ['Apples', 'Oranges', 'Cherries', 'Watermelon'])
plt.show()