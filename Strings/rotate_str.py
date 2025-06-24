def rotateString_brute1(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    for i in range(len(s)):
        s = s[1:] + s[0]  # left shift
        if s == goal:
            return True
    return False

def rotateString_brute2(s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False

    n = len(s)
    for i in range(n):
        rotated = s[i:] + s[:i]
        if rotated == goal:
            return True
    return False

def rotateString_optimal(s: str, goal: str) -> bool:
    return len(s) == len(goal) and goal in (s + s)

print(rotateString_brute1("abcde", "cdeab"))  # True
print(rotateString_brute2("abcde", "cdeab"))  # True
print(rotateString_optimal("abcde", "cdeab"))  # True
