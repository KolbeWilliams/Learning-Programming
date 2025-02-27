#Exercise 3:
#k-means and k-means++
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pandas import DataFrame

def predictFunction(data, centroids, labels):
    predictions = []
    for i in range(len(data)):
        shortest_distance = 1000000
        for j in range(len(centroids)):
            distance = ((data[i][0] - centroids[j][0]) ** 2 + (data[i][1] - centroids[j][1]) ** 2) ** (1/2)
            if distance < shortest_distance:
                shortest_distance = distance
                label = j
        predictions.append(label)
    return predictions

Data = {
'x': [35,34,32,37,33,33,31,27,35,34,62,54,57,47,50,57,59,52,61,47,50,48,39,40,45,47,39,44,50,48],
'y': [79,54,52,77,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,23,22,13,14,22,7,29,25,9,8]
}
#df = DataFrame(Data,columns=['x','y'])
df = DataFrame(Data)
print(df)
#kmeans = KMeans(n_clusters=3).fit(df) #k-means
kmeans = KMeans(n_clusters = 3, init = 'k-means++').fit(df) #k-means++
#EQUIVALENT TO the following two lines:
#kmeans = KMeans(n_clusters=3, init = 'k-means++')
#kmeans = kmeans.fit(df)
centroidsK = kmeans.cluster_centers_ #coordinates of cluster centers (centroids)
labelsK = kmeans.labels_ #labels/clusters each data point belongs to
print(f'Centroids:\n{centroidsK}')
print()
print(f'Labels:\n{labelsK}')

prediction_x = [34, 48, 62, 35]
prediction_y = [52, 6, 49, 77]
new_data = []
for i in range(len(prediction_x)):
    new_data.append([prediction_x[i], prediction_y[i]])
df2 = DataFrame(new_data)
df2.columns = ['x', 'y']
predictions_builtin = kmeans.predict(df2)
print('\nLabel predictions using built in method:\n', predictions_builtin)
predictions = predictFunction(new_data, centroidsK, labelsK)
print('Label predictions using new algorithm:\n', predictions)

#plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float))
plt.scatter(df['x'], df['y'], c = kmeans.labels_) #not necessary: .astype(float)
plt.scatter(centroidsK[:, 0], centroidsK[:, 1], c = 'red', label = 'centroids')
plt.scatter(prediction_x, prediction_y,  label = 'predicted', marker = '+', s = 125)
plt.xlabel('x')
plt.ylabel('y')
plt.title('K = 3')
plt.legend()
plt.show()

