'''Brute Force Circular NGE: [5, 10, 10, -1, 10]
Optimal Circular NGE: [5, 10, 10, -1, 10]  '''
def circular_nge_brute(arr):
    n = len(arr)
    res = [-1] * n
    for i in range(n):
        for j in range(1, n):  # max n-1 steps
            next_idx = (i + j) % n
            if arr[next_idx] > arr[i]:
                res[i] = arr[next_idx]
                break
    return res

def circular_nge_optimal(arr):
    n = len(arr)
    res = [-1] * n
    stack = []  # store indices

    for i in range(2 * n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i % n]:
            stack.pop()
        if stack:
            res[i % n] = arr[stack[-1]]
        stack.append(i % n)
    
    return res

arr = [4, 5, 2, 10, 8]
print("Brute Force Circular NGE:", circular_nge_brute(arr))
print("Optimal Circular NGE:", circular_nge_optimal(arr))