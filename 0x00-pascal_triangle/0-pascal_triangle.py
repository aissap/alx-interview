#!/usr/bin/python3
def pascal_triangle(n):
    """
    Create a function that returns Pascal's triangle up to the nth row.
    """
    triangle = []

    if n <= 0:
        return triangle

    i = 0
    while i < n:
        row = [1]
        for j in range(1, i):
            if j < len(triangle[i - 1]):
                coefficient = triangle[i - 1][j - 1]
            else:
                coefficient = 0
            if j < len(triangle[i - 1]):
                coefficient += triangle[i - 1][j]
            row.append(coefficient)
        row.append(1)
        triangle.append(row)
        i += 1

    return triangle
