#!/usr/bin/python3
def pascal_triangle(n):
	"""
	Generate Pascal's Triangle up to the nth row
	"""
	triangle = []

	if n <= 0:
		return triangle

	triangle.append([1])

	for i in range(n - 1):
		triangle.append([1] + [triangle[i][a] + triangle[i][a + 1]
				for a in range(len(triangle[i]) - 1)] + [1])

	return triangle
