# Maximum Product Subarray

def maxProductSubArray_brute(nums):
    result = float('-inf')
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            prod = 1
            for k in range(i, j + 1):
                prod *= nums[k]
            result = max(result, prod)
    return result

nums = [1, 2, -3, 0, -4, -5]
print("The maximum product subarray:", maxProductSubArray_brute(nums))



def maxProductSubArray_better(nums):
    result = nums[0]
    for i in range(len(nums) - 1):
        p = nums[i]
        for j in range(i + 1, len(nums)):
            result = max(result, p)
            p *= nums[j]
        result = max(result, p)  # manages (n-1)th term
    return result

nums = [1, 2, -3, 0, -4, -5]
print("The maximum product subarray:", maxProductSubArray_better(nums))


def maxProductSubArray_optimal1(arr):
    n = len(arr) # size of array.

    pre, suff = 1, 1
    ans = float('-inf')
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= arr[i]
        suff *= arr[n - i - 1]
        ans = max(ans, max(pre, suff))
    return ans

arr = [1, 2, -3, 0, -4, -5]
print("The maximum product subarray is:", maxProductSubArray_optimal1(arr))


