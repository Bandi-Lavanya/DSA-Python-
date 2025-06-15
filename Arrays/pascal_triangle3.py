# This code generates Pascal's Triangle up to the nth row and prints it.
def nCr_brute(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascal_triangle_brute(n):
    triangle = []
    for row in range(1, n + 1):
        temp = []
        for col in range(1, row + 1):
            temp.append(nCr_brute(row - 1, col - 1))
        triangle.append(temp)
    return triangle

# Example usage
n = 5
result = pascal_triangle_brute(n)
for row in result:
    print(*row)

def generate_row_optimal(row):
    ans = 1
    ans_row = [1]  # inserting the 1st element

    # calculate the rest of the elements:
    for col in range(1, row):
        ans = ans * (row - col)
        ans = ans // col
        ans_row.append(ans)

    return ans_row

def pascal_triangle_optimal(n):
    triangle = []
    
    # store the entire Pascal's triangle
    for row in range(1, n + 1):
        triangle.append(generate_row_optimal(row))
    
    return triangle

# Example usage
n = 5
triangle = pascal_triangle_optimal(n)
for row in triangle:
    print(*row)
