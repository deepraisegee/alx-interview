#!/usr/bin/python3


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Starting with the first row

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Create the next row by adding pairs of adjacent elements from the previous row
        row = (
            [1]
            + [prev_row[j] + prev_row[j + 1] for j in range(len(prev_row) - 1)]
            + [1]
        )
        triangle.append(row)

    return triangle
