'''
Rotate Matrix/ Image - LeetCode 48
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.
'''

def rotate_matrix(matrix):
    # Transpose the matrix
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse the matrix
    for i in range(n):
        s = 0
        e = n - 1
        while s < e:
            matrix[i][s], matrix[i][e] = matrix[i][e], matrix[i][s]
            s += 1
            e -= 1