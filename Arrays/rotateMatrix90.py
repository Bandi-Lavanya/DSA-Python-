def rotate(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]

    return rotated


def rotate_optimal(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example matrix
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

rotated = rotate(arr)

# Print rotated matrix
print("Rotated Image")
for row in rotated:
    for val in row:
        print(val, end=" ")
    print()


rotate_optimal(arr)

# Print rotated matrix
print("Rotated Image")
for row in arr:
    for val in row:
        print(val, end=" ")
    print()