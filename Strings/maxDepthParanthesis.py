def maxDepth(s: str) -> int:
    depth = 0
    max_depth = 0
    for ch in s:
        if ch == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif ch == ')':
            depth -= 1
    return max_depth
print(maxDepth("(1+(2*3)+((8)/4))+1"))  # Output: 3