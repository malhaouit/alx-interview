def pascal_triangle(n):
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
