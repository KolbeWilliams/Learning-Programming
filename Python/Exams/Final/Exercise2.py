#Exercise 2:
import numpy as np
import pandas as pd
#from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('Ex2_dataset.csv', names = ['target class', 'x1', 'x2'])
target_class = np.array(df['target class'])
x1 = np.array(df['x1'])
x2 = np.array(df['x2'])

x_train = []
for i in range(len(x1)):
    x_train.append([x1[i], x2[i]])
x_train = np.array(x_train)
y_train = target_class
x_test = np.array([[3, 3]])
# knn = KNeighborsClassifier(n_neighbors=3).fit(x_train, y_train)
# neighbors = knn.kneighbors(x_test, return_distance=False)
# neighbor_indices = neighbors[0]
# neighbor_classes = y_train[neighbor_indices]

distances = []
for i in range(len(x_train)):
    #distance = np.linalg.norm(x_train[i] - x_test)
    distance = ((x_train[i][0] - x_test[0][0])**2 + (x_train[i][1] - x_test[0][1])**2)**0.5
    distances.append(distance)
distances_sorted = distances.copy()
distances_sorted.sort()
indicies = []
for i in range(len(distances_sorted)):
    for j in range(len(distances)):
        if distances[j] == distances_sorted[i]:
            if j not in indicies:
                indicies.append(j)
                break

neighbor_classes = []
for i in range(3):
    neighbor_classes.append(target_class[indicies[i]])

class_zero = 0
class_one = 0
for i in neighbor_classes:
    if i == 0:
        class_zero += 1
    elif i == 1:
        class_one += 1
if class_zero > class_one:
    print('The data point belongs to class 0')
elif class_one > class_zero:
    print('The data point belongs to class 1')