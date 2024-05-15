import numpy as np
# Operasi Matriks pada Python

# Mengalikan 2 matrix
matrix = [[5,0],
          [1, -2]]

def_mat = [[0 for j in range(2)] for i in range(2)]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        def_mat[i][j] = matrix[i][j] * 2
print(def_mat)

# Versi singkat menggunakan numpy
mat_val = np.array([[5, 0],
                    [1, -2]])
result = mat_val * 2
print(result)
# [[10  0]
#  [ 2 -4]]