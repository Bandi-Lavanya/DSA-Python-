def sort_string(s):
    return ''.join(sorted(s))

def check_anagrams(str1, str2):
    # Case 1: Different lengths
    if len(str1) != len(str2):
        return False

    # Sort both strings
    str1 = sort_string(str1)
    str2 = sort_string(str2)

    # Case 2: Compare character by character
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True

# Main
str1 = "INTEGER"
str2 = "TEGERNI"
print(check_anagrams(str1, str2))


def check_anagrams(str1, str2):
    # Case 1: If the lengths differ, they're not anagrams
    if len(str1) != len(str2):
        return False

    freq = [0] * 26  # For uppercase English letters

    for ch in str1:
        freq[ord(ch) - ord('A')] += 1

    for ch in str2:
        freq[ord(ch) - ord('A')] -= 1

    for count in freq:
        if count != 0:
            return False

    return True

# Main
str1 = "INTEGER"
str2 = "TEGERNI"
print(check_anagrams(str1, str2))
