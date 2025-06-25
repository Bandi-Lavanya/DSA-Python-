#Case 1: Count All Possible Substrings
def count_all_substrings(s: str) -> int:
    n = len(s)
    return n * (n + 1) // 2

# Example
s = "abc"
print(count_all_substrings(s))  # Output: 6
# substrings: "a", "b", "c", "ab", "bc", "abc"


#Case 2: Count All Unique Substrings
def count_unique_substrings(s: str) -> int:
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])
    return len(substrings)

# Example
s = "ababa"
print(count_unique_substrings(s))  # Output: 9
# Unique substrings: 'a', 'ab', 'aba', 'abab', 'ababa', 'b', 'ba', 'bab', 'baba'


#Case 3: Count Number of Times a Substring Occurs in a String
def count_substring_occurrences(s: str, sub: str) -> int:
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            count += 1
    return count

# Example
s = "abababa"
sub = "aba"
print(count_substring_occurrences(s, sub))  # Output: 3
