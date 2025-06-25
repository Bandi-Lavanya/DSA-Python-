def longestPalindrome_brute(s: str) -> str:
    def is_palindrome(sub):
        return sub == sub[::-1]

    max_len = 0
    result = ""
    n = len(s)

    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j+1]) and (j - i + 1 > max_len):
                max_len = j - i + 1
                result = s[i:j+1]
    return result

def longestPalindrome_better(s: str) -> str:
    def expand_from_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome
        odd = expand_from_center(i, i)
        if len(odd) > len(longest):
            longest = odd

        # Even-length palindrome
        even = expand_from_center(i, i+1)
        if len(even) > len(longest):
            longest = even

    return longest
print(longestPalindrome_better("babad"))  # Output: "bab" or "aba"
print(longestPalindrome_brute("babad"))  # Output: "bab" or "aba"