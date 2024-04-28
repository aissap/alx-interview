#!/usr/bin/python3
def pascal_triangle(n):
	triangle = []

	if n <= 0:
		return triangle

	for i in range(n):
		row = [1] * (i + 1)  # Initialize each row with 1s
		if i > 1:
			for j in range(1, i):
				row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
		triangle.append(row)

	return triangle

if __name__ == "__main__":
	triangle = pascal_triangle(5)
	for row in triangle:
		print("[{}]".format(",".join([str(x) for x in row])))
