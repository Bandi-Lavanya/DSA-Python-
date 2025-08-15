'''Prefix: *+AB-CD
Postfix: AB+CD-*'''
def prefix_to_postfix(expression):
    stack = []
    
    # Traverse the expression from right to left
    for char in reversed(expression):
        if char.isalnum():  # Operand
            stack.append(char)
        else:  # Operator
            # Pop two operands from stack
            op1 = stack.pop()
            op2 = stack.pop()
            # Form the postfix expression
            new_expr = op1 + op2 + char
            stack.append(new_expr)
    
    return stack[-1]

# Example
prefix_expr = input("Enter a prefix expression: ")
result = prefix_to_postfix(prefix_expr)
print("Prefix:", prefix_expr)
print("Postfix:", result)
