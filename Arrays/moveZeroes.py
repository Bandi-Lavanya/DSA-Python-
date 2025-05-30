def move_zeros_brutforce(n, a):
    # Temporary list to store non-zero elements
    temp = []

    # Copy non-zero elements to temp
    for i in range(n):
        if a[i] != 0:
            temp.append(a[i])

    # Number of non-zero elements
    nz = len(temp)

    # Fill first nz fields of original list with temp values
    for i in range(nz):
        a[i] = temp[i]

    # Fill the remaining elements with 0
    for i in range(nz, n):
        a[i] = 0

    return a

# Main code
arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = len(arr)
ans = move_zeros_brutforce(n, arr)
print(*ans)


def move_zeros_optimal(n, a):
    j = -1

    # Find the index of the first zero
    for i in range(n):
        if a[i] == 0:
            j = i
            break

    # If there are no zeros, return the array
    if j == -1:
        return a

    # Traverse the array and swap non-zero elements with zeros
    for i in range(j + 1, n):
        if a[i] != 0:
            a[i], a[j] = a[j], a[i]
            j += 1

    return a

# Main code
arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
n = len(arr)
ans = move_zeros_optimal(n, arr)
print(*ans)
