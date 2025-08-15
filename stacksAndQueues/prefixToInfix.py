'''Enter a postfix expression: ABC/-AK/L-*
Postfix: ABC/-AK/L-*
Infix: ((A-(B/C))*((A/K)-L))'''
# Function to check if character is an operator
def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

# Function to convert postfix to infix
def prefix_to_infix(prefix_expr):
    stack = []

    for char in prefix_expr[::-1]:
        if char.isalnum():  # Operand
            stack.append(char)
        elif is_operator(char):
            # Pop two operands from stack
            op1 = stack.pop()
            op2 = stack.pop()
            # Combine into an infix string with parentheses
            new_expr = "(" + op1 + char + op2+ ")"
            stack.append(new_expr)

    # Final element in stack is the infix expression
    return stack[-1]

# Example usage
prefix = input("Enter a prefix expression: ")
print("Prefix Expression:", prefix)
infix = prefix_to_infix(prefix)
print("Infix Expression:", infix)