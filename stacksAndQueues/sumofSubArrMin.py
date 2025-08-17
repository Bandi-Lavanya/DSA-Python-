def sumSubarrayMins_brute(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(i, n):
            total += min(arr[i:j+1])   # O(n) for min()
    return total

print(sumSubarrayMins_brute([3,1,2,4]))  # 17
def sumSubarrayMins_better(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        curr_min = arr[i]
        for j in range(i, n):
            curr_min = min(curr_min, arr[j])  # O(1)
            total += curr_min
    return total

print(sumSubarrayMins_better([3,1,2,4]))  # 17
def sumSubarrayMins_optimal(arr):
    n = len(arr)
    MOD = 10**9 + 7

    # Find Previous Smaller
    prev = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        prev[i] = stack[-1] if stack else -1
        stack.append(i)

    # Find Next Smaller
    next_sm = [n] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        next_sm[i] = stack[-1] if stack else n
        stack.append(i)

    # Calculate contribution
    total = 0
    for i in range(n):
        left = i - prev[i]
        right = next_sm[i] - i
        total += arr[i] * left * right
    return total % MOD

print(sumSubarrayMins_optimal([3,1,2,4]))  # 17
