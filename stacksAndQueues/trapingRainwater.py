def trap_brute(arr):
    n = len(arr)
    waterTrapped = 0
    for i in range(n):
        j = i
        leftMax = 0
        rightMax = 0
        while j >= 0:
            leftMax = max(leftMax, arr[j])
            j -= 1
        j = i
        while j < n:
            rightMax = max(rightMax, arr[j])
            j += 1
        waterTrapped += min(leftMax, rightMax) - arr[i]
    return waterTrapped

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"The water that can be trapped is {trap_brute(arr)}")


def trap_better(arr):
    n = len(arr)
    prefix = [0] * n
    suffix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], arr[i])
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = max(suffix[i + 1], arr[i])
    waterTrapped = 0
    for i in range(n):
        waterTrapped += min(prefix[i], suffix[i]) - arr[i]
    return waterTrapped

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"The water that can be trapped is {trap_better(arr)}")



def trap_optimal(height):
    n = len(height)
    left = 0
    right = n-1
    res = 0
    maxLeft = 0
    maxRight = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                res += maxLeft - height[left]
            left += 1
        else:
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                res += maxRight - height[right]
            right -= 1
    return res
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"The water that can be trapped is {trap_optimal(arr)}")