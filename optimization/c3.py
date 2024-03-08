import numpy as np

def znajdz_cykl_C3(matrix):
    n = len(matrix)
    for v in range(n):
        for u in range(n):
            if matrix[v][u] == 1:
                for w in range(n):
                    if matrix[v][w] == 1 and matrix[u][w] == 1:
                        return [v, u, w]
    return None


def czy_istnieje_cykl_C3(macierz_sasiedztwa):
    macierz_sasiedztwa_3 = np.linalg.matrix_power(macierz_sasiedztwa, 3)
    
    for i in range(len(macierz_sasiedztwa)):
        if macierz_sasiedztwa_3[i][i] > 0:
            return "TAK"
    return "NIE"



n = 5
macierz_sasiedztwa = np.zeros((n, n))
macierz_sasiedztwa[0][1] = 1
macierz_sasiedztwa[1][0] = 1
macierz_sasiedztwa[1][2] = 1
macierz_sasiedztwa[2][1] = 1
macierz_sasiedztwa[2][3] = 1
macierz_sasiedztwa[3][2] = 1
macierz_sasiedztwa[3][4] = 1
macierz_sasiedztwa[4][3] = 1
macierz_sasiedztwa[4][0] = 1
macierz_sasiedztwa[0][4] = 1

print(czy_istnieje_cykl_C3(macierz_sasiedztwa))