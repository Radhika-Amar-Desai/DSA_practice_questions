import sys
from functools import lru_cache

def mcm (matrix_dim : list, i = 1, j = 1):

    if (i >= j):
        return 0

    min_ans = sys.maxsize

    for k in range (i, j):
        temp_ans = mcm(matrix_dim, i, k) + mcm (matrix_dim, k + 1, j) \
                    + matrix_dim[i - 1] * matrix_dim[k] * matrix_dim[j]

        min_ans = min(temp_ans, min_ans)

    return min_ans

matrix_dim = [40,20,30,10,30,60,100]
print(mcm(matrix_dim, i = 1, j = len(matrix_dim) - 1))

def mcm_dp ( matrix_dim ):
    dp = [[0 for _ in range(len(matrix_dim))] for _ in range(len(matrix_dim))]

    def fill_dp():
        for row_index in range(0, len(matrix_dim)):
            for col_index in range(0, len(matrix_dim)):

                if row_index + 1 < col_index:
                    dp[row_index][col_index] = min([dp[row_index][k] + dp[k][col_index] + \
                                                    matrix_dim[row_index] * matrix_dim[k] * matrix_dim[col_index]\
                                                    for k in range(row_index + 1, col_index)])
    
    for _ in range(len(matrix_dim)):
        fill_dp()

    return dp[0][-1]

print ( mcm_dp(matrix_dim) )