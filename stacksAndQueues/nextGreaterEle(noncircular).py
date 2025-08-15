'''Brute Force NGE: [5, 10, 10, -1, -1]
Optimal NGE: [5, 10, 10, -1, -1]'''
def nge_brute(arr):
    n = len(arr)
    res = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
    return res

def nge_optimal(arr):
    n = len(arr)
    res = [-1] * n
    stack = []  # store elements, not indices

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    
    return res

arr = [4, 5, 2, 10, 8]
print("Brute Force NGE:", nge_brute(arr))
print("Optimal NGE:", nge_optimal(arr))