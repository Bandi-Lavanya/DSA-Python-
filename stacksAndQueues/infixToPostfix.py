'''Infix expression: (p+q)*(m-n)
Postfix expression: pq+mn-*'''
def precedence(ch):
    """Return precedence of a given operator."""
    if ch in ('+', '-'):
        return 1
    elif ch in ('*', '/'):
        return 2
    elif ch == '^':
        return 3
    return -1


def infix_to_postfix(expression):
    """Convert infix expression to postfix expression."""
    result = ""  # output string
    stack = []   # stack for operators

    for c in expression:
        # If character is operand (letter or digit), add to output
        if c.isalnum():
            result += c

        # If character is '(', push to stack
        elif c == '(':
            stack.append(c)

        # If character is ')', pop until '(' is found
        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # remove '(' from stack

        # If character is an operator
        else:
            while stack and precedence(c) <= precedence(stack[-1]):
                result += stack.pop()
            stack.append(c)

    # Pop remaining operators from stack
    while stack:
        if stack[-1] == '(':
            return "Invalid Expression"
        result += stack.pop()

    return result


# Example usage
exp = input()
print("Infix expression:", exp)
print("Postfix expression:", infix_to_postfix(exp))
