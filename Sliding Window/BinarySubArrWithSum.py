def numSubarraysWithSum_brute(nums, goal):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if sum(nums[i:j+1]) == goal:   # recomputing sum → O(n)
                count += 1
    return count

# Example
print(numSubarraysWithSum_brute([1,0,1,0,1], 2))  # Output: 4

def numSubarraysWithSum_better(nums, goal):
    n = len(nums)
    count = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            if curr_sum == goal:
                count += 1
    return count

# Example
print(numSubarraysWithSum_better([1,0,1,0,1], 2))  # Output: 4

def numSubarraysWithSum(nums, goal):
    def atMost(k):
        if k < 0:  # edge case
            return 0
        left = 0
        curr_sum = 0
        count = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            
            while curr_sum > k:
                curr_sum -= nums[left]
                left += 1
            
            count += (right - left + 1)  # all subarrays ending at right
        return count
    
    return atMost(goal) - atMost(goal - 1)


# Example test cases
print(numSubarraysWithSum([1,0,1,0,1], 2))  # 4
print(numSubarraysWithSum([0,0,0,0,0], 0))  # 15
