'''
    2D Lists
    Given 2D list calculate the sum of diagonal elements.
'''

def diagonal_sum(matrix):
    diagonalSum = 0
    for i in range(len(matrix)):
        diagonalSum = matrix[i][i]
    return diagonalSum