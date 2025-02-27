#Exercise 4:
import numpy as np

def matrixMultiply(A, B):
    if A.shape[1] != B.shape[0]:
        print('Matricies cannot be multiplied')
    else:
        result = np.zeros((A.shape[0], B.shape[1]))
        for i in range(len(A)):
            for x in range(len(B[0])):
                for j in range(len(A[0])):
                    result[i][x] += A[i][j] * B[j][x]
        return(result)

A = np.array([[2, 3],
              [7, 9]])

B = np.array([[3, 7, 8],
              [6, 1, 2]])

print('Using built-in method:\n', np.matmul(A, B))
print('\nUsing new function:\n', matrixMultiply(A, B))