#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
    n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list of lists: A list of lists where each inner list represents a row in Pascal's Triangle.
                   Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []
    
    triangle = []
    
    for i in range(n):
        # Start each row with 1
        row = [1] * (i + 1)
        
        # Calculate the inner elements of the row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Append the row to the triangle
        triangle.append(row)
    
    return triangle

if __name__ == "__main__":
    from 0-main import print_triangle
    print_triangle(pascal_triangle(5))
