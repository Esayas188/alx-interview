#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        previous_row = triangle[-1]
        current_row = [1]

        for i in range(1, len(previous_row)):
            current_row.append(previous_row[i - 1] + previous_row[i])

        current_row.append(1)
        triangle.append(current_row)

    return triangle
