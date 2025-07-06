def withoutrepeat(s):
    maxs=""
    for i in range(len(s)):
        for j in range(i,len(s)):
            if len(set(s[i:j+1]))==len(s[i:j+1]):
                if(len(s[i:j+1]) > len(maxs)):
                    maxs=s[i:j+1]
    return maxs
print("The max unique sub string is :",withoutrepeat("abcabcbb"))  # Output: "abc"