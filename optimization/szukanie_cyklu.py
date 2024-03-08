import numpy as np

def force_method(matrix):
    n = len(matrix)
    for v in range(n):
        for u in range(n):
            if matrix[v][u] == 1:
                for w in range(n):
                    if matrix[v][w] == 1 and matrix[u][w] == 1:
                        return [v, u, w]
    return None

def multiplication_method(matrix, path_length=3):
    matrix_tmp = np.linalg.matrix_power(matrix, path_length)
    for i in range(len(matrix)):
        if matrix_tmp[i][i] > 0:
            return True
    return False