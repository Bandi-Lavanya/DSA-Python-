'''fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output = 5
'''
def totalFruits_brute(fruits):
    n = len(fruits)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            distinct = set(fruits[i:j+1])
            if len(distinct) <= 2:
                ans = max(ans, j - i + 1)
    return ans
print(totalFruits_brute([3,3,3,1,2,1,1,2,3,3,4])) 

def totalFruits_better(fruits):
    n = len(fruits)
    ans = 0
    for i in range(n):
        freq = {}
        for j in range(i, n):
            freq[fruits[j]] = freq.get(fruits[j], 0) + 1
            if len(freq) <= 2:
                ans = max(ans, j - i + 1)
            else:
                break
    return ans
print(totalFruits_better([3,3,3,1,2,1,1,2,3,3,4]))

def totalFruits(fruits):
    from collections import defaultdict
    left = 0
    freq = defaultdict(int)
    ans = 0

    for right in range(len(fruits)):
        freq[fruits[right]] += 1

        while len(freq) > 2:  # too many fruit types
            freq[fruits[left]] -= 1
            if freq[fruits[left]] == 0:
                del freq[fruits[left]]
            left += 1

        ans = max(ans, right - left + 1)

    return ans
print(totalFruits([3,3,3,1,2,1,1,2,3,3,4]))