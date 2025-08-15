'''Postfix: ABC/-AK/L-*
Prefix : *-A/BC-/AKL'''

def postfix_to_prefix(postfix):
    stack = []

    for ch in postfix:
        if ch.isalnum():  # operand
            stack.append(ch)
        else:  # operator
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = ch + op1 + op2  # prefix form
            stack.append(new_expr)

    return stack[-1]

# Example
postfix_expr = "ABC/-AK/L-*"
prefix_expr = postfix_to_prefix(postfix_expr)
print("Postfix:", postfix_expr)
print("Prefix :", prefix_expr)
