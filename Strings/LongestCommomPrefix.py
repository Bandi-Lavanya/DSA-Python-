def longestCommonPrefix_brute(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):  # iterate over each character in first string
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]  # mismatch found
    return strs[0]  # entire first string is a prefix


def longestCommonPrefix_optimal(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):  # iterate over each character in first string
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]  # mismatch found
    return strs[0]  # entire first string is a prefix

strs = ["flower", "flow", "flight"]
print("The longest substring is: ",longestCommonPrefix_brute(strs))  
print("The longest substring is: ",longestCommonPrefix_optimal(strs))
