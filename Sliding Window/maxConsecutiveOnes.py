'''Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6  (subarray [0,0,1,1,1,1] or [1,1,1,1,0,1])
'''
def longestOnes_brute(nums, k):
    n = len(nums)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            zeroes = 0
            for t in range(i, j+1):
                if nums[t] == 0:
                    zeroes += 1
            if zeroes <= k:
                ans = max(ans, j-i+1)
    return ans
print(longestOnes_brute([1,1,1,0,0,0,1,1,1,1,0], 2))

def longestOnes_better(nums, k):
    n = len(nums)
    ans = 0
    for i in range(n):
        zeroes = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeroes += 1
            if zeroes <= k:
                ans = max(ans, j-i+1)
            else:
                break   # no need to go further
    return ans
print(longestOnes_better([1,1,1,0,0,0,1,1,1,1,0], 2))

def longestOnes(nums, k):
    left = 0
    zeroes = 0
    ans = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroes += 1
        while zeroes > k:
            if nums[left] == 0:
                zeroes -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
