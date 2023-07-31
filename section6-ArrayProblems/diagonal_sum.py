'''
    2D Lists
    Given 2D list calculate the sum of diagonal elements.
'''

def diagonal_sum(matrix):
    diagonalSum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == j:
                diagonalSum += matrix[i][j]
    return diagonalSum