def nse_brute(arr):
    n = len(arr)
    res = [-1] * n
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] < arr[i]:
                res[i] = arr[j]
                break
    return res

# Example
print(nse_brute([4, 8, 5, 2, 25]))  # Output: [2, 5, 2, -1, -1]

def nse_optimal(arr):
    n = len(arr)
    res = [-1] * n
    stack = []
    
    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    
    return res

# Example
print(nse_optimal([4, 8, 5, 2, 25]))  # Output: [2, 5, 2, -1, -1]

def circular_nse_brute(arr):
    n = len(arr)
    res = [-1] * n
    for i in range(n):
        for j in range(1, n):  # check next n-1 positions
            next_idx = (i + j) % n
            if arr[next_idx] < arr[i]:
                res[i] = arr[next_idx]
                break
    return res

# Example
print(circular_nse_brute([4, 8, 5, 2, 25]))  
# Output: [2, 5, 2, -1, 4]
def circular_nse_optimal(arr):
    n = len(arr)
    res = [-1] * n
    stack = []  # stores indices
    
    for i in range(2 * n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i % n]:
            stack.pop()
        if stack:
            res[i % n] = arr[stack[-1]]
        stack.append(i % n)
    
    return res

# Example
print(circular_nse_optimal([4, 8, 5, 2, 25]))  
# Output: [2, 5, 2, -1, 4]
