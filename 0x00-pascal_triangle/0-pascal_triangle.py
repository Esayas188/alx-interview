#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row [1]

    for i in range(1, n):
        previous_row = triangle[i - 1]
        current_row = [1]  # First element of the row is always 1

        for j in range(1, i):
            # Each element in the middle of the row is the sum of the two elements above it
            current_row.append(previous_row[j - 1] + previous_row[j])

        current_row.append(1)  # Last element of the row is always 1
        triangle.append(current_row)

    return triangle
