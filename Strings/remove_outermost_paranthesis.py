def removeOuterParentheses_brute(s: str) -> str:
    res = []
    balance = 0
    start = 0

    for i, ch in enumerate(s):
        if ch == '(':
            balance += 1
        else:
            balance -= 1

        if balance == 0:
            # we found a primitive substring from start to i
            res.append(s[start + 1:i])  # remove outermost
            start = i + 1

    return ''.join(res)


def removeOuterParentheses_better(s: str) -> str:
    res = []
    balance = 0

    for ch in s:
        if ch == '(':
            if balance > 0:
                res.append(ch)
            balance += 1
        else:
            balance -= 1
            if balance > 0:
                res.append(ch)

    return ''.join(res)

s="(()())(())(()(()))"
print(removeOuterParentheses_brute(s))
print(removeOuterParentheses_better(s))