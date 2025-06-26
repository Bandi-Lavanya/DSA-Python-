def beautySum(s: str) -> int:
    total_beauty = 0
    n = len(s)

    for i in range(n):
        freq = [0] * 26  # Frequency array for characters a-z
        for j in range(i, n):
            idx = ord(s[j]) - ord('a')
            freq[idx] += 1

            max_freq = max(freq)
            min_freq = min([f for f in freq if f > 0])
            total_beauty += max_freq - min_freq

    return total_beauty

def beautySum_brute(s: str) -> int:
    n = len(s)
    total = 0

    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            freq = {}
            for ch in sub:
                freq[ch] = freq.get(ch, 0) + 1
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            total += max_freq - min_freq

    return total

print(beautySum("aabcb"))  # Output: 5
print(beautySum_brute("aabcb"))  # Output: 5