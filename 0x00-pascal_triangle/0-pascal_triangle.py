#!/usr/bin/python3
def pascal_triangle(n):
    """
    Create a function that returns Pascal's triangle up to the nth row.
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [1] 
        for j in range(1, i + 1):
            coefficient = triangle[i - 1][j - 1] if j < len(triangle[i - 1]) else 0
            coefficient += triangle[i - 1][j] if j < len(triangle[i - 1]) else 0
            row.append(coefficient)
        triangle.append(row)

    return triangle
