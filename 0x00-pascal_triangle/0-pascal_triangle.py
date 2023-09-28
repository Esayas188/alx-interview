#!/usr/bin/python3
def pascal_triangle(n):
    res = []
    if n > 0:
        for i in range(n):
            level = []
            C = 1
            for j in range(i + 1):
                level.append(C)
                C = C * (i - j) // (j + 1)
            res.append(level)
    return res
