# Function to find the maximum number of consecutive 1's in a binary array
def findMaxConsecutiveOnes(nums):
    cnt = 0
    maxi = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
        else:
            cnt = 0
        maxi = max(maxi, cnt)
    return maxi



nums = [1, 1, 0, 1, 1, 1]
ans = findMaxConsecutiveOnes(nums)
print("The maximum  consecutive 1's are", ans)