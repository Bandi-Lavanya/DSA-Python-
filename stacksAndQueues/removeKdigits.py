def removeKdigits_better(num: str, k: int) -> str:
    num = list(num)
    
    for _ in range(k):
        i = 0
        # find the first peak (digit > next digit)
        while i < len(num)-1 and num[i] <= num[i+1]:
            i += 1
        num.pop(i)
    
    # remove leading zeros
    result = ''.join(num).lstrip("0")
    return result if result else "0"

print(removeKdigits_better("1432219", 3))  # 1219

def removeKdigits_optimal(num: str, k: int) -> str:
    stack = []
    
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If k > 0, remove from the end
    stack = stack[:-k] if k else stack
    
    # Convert back to string and remove leading zeros
    result = ''.join(stack).lstrip("0")
    return result if result else "0"

print(removeKdigits_optimal("1432219", 3))  # 1219
