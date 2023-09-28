#!/usr/bin/python3
def pascal_triangle(n):
  """
  Returns a list of lists of integers representing the Pascal's triangle of n.

  Args:
    n: The number of rows in the Pascal's triangle.

  Returns:
    A list of lists of integers representing the Pascal's triangle of n.
  """

  if n <= 0:
    return []

  triangle = [[1]]
  for i in range(1, n):
    row = []
    for j in range(i + 1):
      if j == 0 or j == i:
        row.append(1)
      else:
        row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    triangle.append(row)
  return triangle
