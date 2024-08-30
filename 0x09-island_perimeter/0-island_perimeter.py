#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    :param grid: List[List[int]], 2D list representing the grid
    :return: int, perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the bottom
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
