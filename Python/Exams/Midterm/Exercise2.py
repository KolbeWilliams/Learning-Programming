#Transpose Matrix
import numpy as np

def transposeFunc(matrix):
    numRows = len(matrix)
    numCols = len(matrix[0])
    transposed = np.zeros((numCols, numRows))
    for i in range(numRows):
        for j in range(numCols):
            transposed[j][i] = matrix[i][j]
    return transposed

matrix = np.array([[3, 4, 5],
                   [6, 7, 8]])

print('Using Built-in Function:\n', matrix.T)
print(f'\nUsing My Function:\n {transposeFunc(matrix)} \n')