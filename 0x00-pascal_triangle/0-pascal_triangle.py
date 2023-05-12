#!/usr/bin/python3
'''
Module of Pascal's triangle of n
'''


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = [1]
    for i in range(1, n):
        row = [1]
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                coefficient = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(coefficient)
        triangle.append(row)
    return triangle
