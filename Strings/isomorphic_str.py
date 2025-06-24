def isIsomorphic_brute(s, t):
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j] and t[i] != t[j]:
                return False
            if s[i] != s[j] and t[i] == t[j]:
                return False
    return True


def isIsomorphic_better(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for sc, tc in zip(s, t):
        if (sc in s_to_t and s_to_t[sc] != tc) or (tc in t_to_s and t_to_s[tc] != sc):
            return False
        s_to_t[sc] = tc
        t_to_s[tc] = sc

    return True

def isIsomorphic_optimal(s, t):
    def encode(word):
        mapping = {}
        code = []
        index = 0
        for ch in word:
            if ch not in mapping:
                mapping[ch] = index
                index += 1
            code.append(mapping[ch])
        return code

    return encode(s) == encode(t)
print(isIsomorphic_brute("egg", "add"))  # True
print(isIsomorphic_better("egg", "add"))  # True
print(isIsomorphic_optimal("egg", "add"))  # True
