#Exercise 4:
#elbow method
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pandas import DataFrame
import pandas as pd
import numpy as np
import math
Data = {
'x':[35,34,32,37,33,33,31,27,35,34,62,54,57,47,50,57,59,52,61,47,50,48,39,40,45,47,39,44,50,48],
'y':[79,54,52,77,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,23,22,13,14,22,7,29,25,9,8]
}
df = DataFrame(Data,columns=['x','y'])
distances = []
K = range(1,10)
for k in K:
    ClusterInfo = kmeanModel = KMeans(n_clusters=k).fit(df) #cluster data points
    distances.append(ClusterInfo.inertia_) #append distances to the list: distances

#find the smallest angle out of all the points to find the elbow
#I'm not sure if this is the correct approach, but finding the elbow visually
#seems to consist of finding the point with the smallest angle.
smallest_angle = 2 * math.pi
clusters = 0
for i in range(len(K) - 2):
    slope1 = (distances[i + 1] - distances[i]) / (K[i + 1] - K[i])
    slope2 = (distances[i + 2] - distances[i + 1]) / (K[i + 2] - K[i + 1])
    angle = np.arctan(abs((slope1 - slope2) / (1 + slope1 * slope2)))
    if angle < smallest_angle:
        smallest_angle = angle
        clusters = K[i]
print('The optimal number of clusters is:', clusters)

plt.plot(K, distances, 'bo-') #print distances
plt.xlabel('K-Clusters')
plt.ylabel('Distance')
plt.title('Cluster Values and Distances')
plt.show()

