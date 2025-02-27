#Exercise 1:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('Mall_customers.csv')
df.columns = ['Customer', 'Genre', 'Age', 'Income', 'Spending']
df['Genre'] = list(map(lambda x: 0 if x == 'Female' else 1, df['Genre']))
print(df) #Use print(df.to_string()) to print the entire dataframe

x = np.array(df['Age'])
y = np.array(df['Income'])
data = []
for i in range(len(df['Age'])):
    data.append([x[i], y[i]])
n_clusters = 4
kmeans = KMeans(n_clusters = n_clusters).fit(data)
centroidsK = kmeans.cluster_centers_
labelsK = kmeans.labels_

plt.scatter(x, y, c = labelsK)
plt.scatter(centroidsK[:, 0], centroidsK[:, 1], c = 'r', label = 'centroids')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title(f'K = {n_clusters}')
plt.legend()
plt.show()
