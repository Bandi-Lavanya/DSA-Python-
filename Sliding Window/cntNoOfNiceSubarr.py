'''Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].'''
def numberOfSubarrays_bruteforce(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            odds = 0
            for x in nums[i:j+1]:
                if x % 2 == 1:
                    odds += 1
            if odds == k:
                count += 1
    return count

# Example
print(numberOfSubarrays_bruteforce([1,1,2,1,1], 3))  # 2

def numberOfSubarrays_better(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        odds = 0
        for j in range(i, n):
            if nums[j] % 2 == 1:
                odds += 1
            if odds == k:
                count += 1
            elif odds > k:  # stop early
                break
    return count

print(numberOfSubarrays_better([1,1,2,1,1], 3))  # 2

def numberOfSubarrays_optimal1(nums, k):
    def atMost(k):
        left = 0
        res = 0
        odds = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odds += 1
            while odds > k:
                if nums[left] % 2 == 1:
                    odds -= 1
                left += 1
            res += (right - left + 1)
        return res
    
    return atMost(k) - atMost(k - 1)

print(numberOfSubarrays_optimal1([1,1,2,1,1], 3))  # 2

def numberOfSubarrays_optimal2(nums, k):
    n = len(nums)
    left = 0
    right = 0
    count = 0
    odds = 0
    
    while right < n:
        if nums[right] % 2 == 1:
            odds += 1
        
        # If we have more than k odds, shrink from left
        while odds > k:
            if nums[left] % 2 == 1:
                odds -= 1
            left += 1
        
        # If exactly k odds, count subarrays
        if odds == k:
            temp = left
            # skip extra even numbers on left
            while nums[temp] % 2 == 0:
                temp += 1
            # number of valid starts = (temp - left + 1)
            count += (temp - left + 1)
        
        right += 1
    
    return count


print(numberOfSubarrays_optimal2([1,1,2,1,1], 3))  # 2
print(numberOfSubarrays_optimal2([2,4,6], 1))      # 0
print(numberOfSubarrays_optimal2([2,2,2,1,2,2,1,2,2,2], 2))  # 16
