import random


def matrixGenerator(m, n, min_limit=0, max_limit=9):
    a = [[random.randint(min_limit, max_limit) for i in range(n)] for j in range(m)]
    for i in range(m):
        print(a[i])
    return a


def bubbleSort(matrix, m, n):
    for str in range(m-1, -1, -1):
        for i in range(0, min(m-str-1, n-1), +1):
            for j in range(0, min(m - str - 1, n-1), +1):
                if matrix[str + j][j] > matrix[str + j + 1][j + 1]:
                    #print(matrix[j + str][j], matrix[j + str + 1][j + 1])
                    swapM(matrix, j + str, j, j + str + 1, j + 1)
                    # for k in range(5):
                    #     print(a[k])

    for clm in range(1, n, +1):
        for j in range(0, min(n - clm - 1, m - 1)):
            for i in range(0, min(n - clm - 1, m - 1)):
                if matrix[i][i + clm] > matrix[i + 1][i + clm + 1]:
                    swapM(matrix, i, i + clm, i + 1, i + clm + 1)

    return matrix


def swapM(mat, ai, aj, bi, bj):
    mat[ai][aj], mat[bi][bj] = mat[bi][bj], mat[ai][aj]


# a = matrixGenerator(8, 6, 0, 9)
# a = bubbleSort(a, 8, 6)
# print('')
# for i in range(8):
#     print(a[i])

m = int(input('Количество строк: '))
n = int(input('Количество столбцов: '))

a = matrixGenerator(m, n)
bubbleSort(a, m, n)

print('')
for i in range(m):
    print(a[i])