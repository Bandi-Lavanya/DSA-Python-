def countPartitions(a, maxSum):
    n = len(a)  # size of array
    partitions = 1
    subarraySum = 0
    for i in range(n):
        if subarraySum + a[i] <= maxSum:
            # insert element to current subarray
            subarraySum += a[i]
        else:
            # insert element to next subarray
            partitions += 1
            subarraySum = a[i]
    return partitions

def largestSubarraySumMinimized(a, k):
    low = max(a)
    high = sum(a)

    for maxSum in range(low, high+1):
        if countPartitions(a, maxSum) == k:
            return maxSum
    return low

a = [10, 20, 30, 40]
k = 2
ans = largestSubarraySumMinimized(a, k)
print("The answer is:", ans)

