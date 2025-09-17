'''Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.'''
def maxScore_brute(cardPoints, k):
    n = len(cardPoints)
    maxScore = 0

    for i in range(k+1):  
        left_sum = sum(cardPoints[:i])  
        right_sum = sum(cardPoints[n-(k-i):])  
        maxScore = max(maxScore, left_sum + right_sum)

    return maxScore
print(maxScore_brute([1,2,3,4,5,6,1], 3))  # 12

def maxScore_better(cardPoints, k):
    n = len(cardPoints)
    prefix = [0] * (k+1)
    suffix = [0] * (k+1)

    # prefix sums
    for i in range(1, k+1):
        prefix[i] = prefix[i-1] + cardPoints[i-1]

    # suffix sums
    for i in range(1, k+1):
        suffix[i] = suffix[i-1] + cardPoints[-i]

    maxScore = 0
    for i in range(k+1):
        maxScore = max(maxScore, prefix[i] + suffix[k-i])

    return maxScore
print(maxScore_better([1,2,3,4,5,6,1], 3))  # 12

def maxScore_optimal(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints)

    if k == n:  # must take all cards
        return total

    window = n - k
    curr_sum = sum(cardPoints[:window])
    min_sum = curr_sum

    for i in range(window, n):
        curr_sum += cardPoints[i] - cardPoints[i-window]
        min_sum = min(min_sum, curr_sum)

    return total - min_sum
print(maxScore_optimal([1,2,3,4,5,6,1], 3))  # 12
print(maxScore_optimal([2,2,2], 2))  # 4