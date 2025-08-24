'''Input: AAABBCCD, k = 2
Output: 5'''
def characterReplacement_bruteforce(s, k):
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            freq = {}
            for ch in substring:
                freq[ch] = freq.get(ch, 0) + 1
            max_freq = max(freq.values())
            if (len(substring) - max_freq) <= k:
                ans = max(ans, len(substring))
    return ans
print(characterReplacement_bruteforce("AAABBCCD", 2))

def characterReplacement_better(s, k):
    n = len(s)
    ans = 0
    for i in range(n):
        freq = {}
        max_freq = 0
        for j in range(i, n):
            freq[s[j]] = freq.get(s[j], 0) + 1
            max_freq = max(max_freq, freq[s[j]])
            
            if (j - i + 1) - max_freq <= k:
                ans = max(ans, j - i + 1)
    return ans
print(characterReplacement_better("AAABBCCD", 2))

def characterReplacement(s, k):
    from collections import defaultdict
    count = defaultdict(int)
    left = 0
    max_freq = 0
    ans = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])
        
        # If more than k replacements needed → shrink window
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
    
    return ans
print(characterReplacement("AAABBCCD", 2))