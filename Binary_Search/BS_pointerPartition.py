def PartionsCount(arr,maxSum):
    partitions=1
    subarraySum=0
    for part in range(len(arr)):
        if(subarraySum + arr[part] <= maxSum):
            subarraySum += arr[part]
        else:
            partitions +=1
            subarraySum = arr[part]
    return partitions

def largestSubarraySumMinimized(a, k):
    low = max(a)
    high = sum(a)
    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        partitions = PartionsCount(a, mid)
        if partitions > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

a = [10, 20, 30, 40]
k = 2
ans = largestSubarraySumMinimized(a, k)
print("The answer is:", ans)