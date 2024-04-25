#!/usr/bin/python3
def pascal_triangle(n):
	"""
	Generate Pascal's Triangle up to the nth row
	"""
	triangle = []

	if n <= 0:
		return triangle

	triangle.append([1])

	for i in range(1, n):
		row = [1]

		for j in range(1, i):
			prev_row_len = len(triangle[i - 1])
			prev_left = triangle[i - 1][j - 1] if j - 1 < prev_row_len else 0
			prev_right = triangle[i - 1][j] if j < prev_row_len else 0
			row.append(prev_left + prev_right)	

		row.append(1)

		triangle.append(row)

	return triangle
