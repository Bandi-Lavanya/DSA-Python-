def withoutrepeat_brute(s):
    max_sub = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(set(s[i:j+1])) == len(s[i:j+1]):
                if len(s[i:j+1]) > len(max_sub):
                    max_sub = s[i:j+1]
    return max_sub

print(withoutrepeat_brute("abcabcbb"))  # Output: "abc"

def withoutrepeat_better(s):
    max_sub = ""
    n = len(s)

    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            if j - i + 1 > len(max_sub):
                max_sub = s[i:j+1]

    return max_sub

print(withoutrepeat_better("abcabcbb"))  # Output: "abc"


def withoutrepeat(s):
    char_index = {}     # Stores last index of each character
    left = 0            # Start of the current window
    max_len = 0
    start = 0           # Start index of the longest substring

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            # Found a repeat → move the left pointer past the last occurrence
            left = char_index[s[right]] + 1
        char_index[s[right]] = right
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return s[start:start + max_len]

print(withoutrepeat("abcabcbb"))  # Output: "abc"

