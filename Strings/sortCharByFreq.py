def frequencySort_brute(s: str) -> str:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    result = ''
    for _ in range(len(s)):
        max_char = ''
        max_freq = 0
        for ch in freq:
            if freq[ch] > max_freq:
                max_char = ch
                max_freq = freq[ch]
        result += max_char * max_freq
        freq[max_char] = 0  # Mark as used
    return result

from collections import Counter

def frequencySort_better(s: str) -> str:
    freq = Counter(s)
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    result = ''
    for ch, count in sorted_chars:
        result += ch * count
    return result

from collections import Counter

def frequencySort_optimal(s: str) -> str:
    freq = Counter(s)  # Step 1: Count frequencies
    max_freq = max(freq.values())  # Step 2: Get highest frequency

    # Step 3: Create buckets of size max_freq + 1
    buckets = [[] for i in range(max_freq + 1)]

    # Step 4: Place characters into buckets according to frequency
    for ch, count in freq.items():
        buckets[count].append(ch)

    # Step 5: Build result from high to low frequency
    result = ''
    for i in range(max_freq, 0, -1):
        for ch in buckets[i]:
            result += ch * i
    return result


print(frequencySort_brute("tree"))  # "eetr" or "eert"
print(frequencySort_better("tree"))  
print(frequencySort_optimal("tree"))  