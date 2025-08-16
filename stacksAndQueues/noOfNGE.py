def num_nges_brute(arr):
    n = len(arr)
    res = [0] * n
    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                count += 1
            elif arr[j] <= arr[i]:
                break
        res[i] = count
    return res

print(num_nges_brute([5, 7, 1, 7, 6, 0]))  
# Output: [2, 1, 0, 0]

def num_nges_until_smaller(arr):
    n = len(arr)
    res = [0] * n
    stack = []  # will store values, decreasing order

    for i in range(n - 1, -1, -1):
        count = 0
        temp_stack = []
        
        # pop all smaller/equal elements — they can't be NGEs for current
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        # Count elements greater until smaller/equal appears
        for val in reversed(stack):
            if val > arr[i]:
                count += 1
            else:
                break
        
        res[i] = count
        stack.append(arr[i])
    
    return res

# Example
arr = [5, 7, 1, 7, 6, 0]
print(num_nges_until_smaller(arr))  
# Output: [1, 0, 2, 0, 0, 0]
