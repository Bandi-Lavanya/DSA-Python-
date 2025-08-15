'''Enter a postfix expression: ABC/-AK/L-*
Postfix: ABC/-AK/L-*
Infix: ((A-(B/C))*((A/K)-L))'''
# Function to check if character is an operator
def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

# Function to convert postfix to infix
def postfix_to_infix(postfix):
    stack = []

    for char in postfix:
        if char.isalnum():  # Operand
            stack.append(char)
        elif is_operator(char):
            # Pop two operands from stack
            op1 = stack.pop()
            op2 = stack.pop()
            # Combine into an infix string with parentheses
            new_expr = "(" + op2 + char + op1 + ")"
            stack.append(new_expr)

    # Final element in stack is the infix expression
    return stack[-1]

# Example usage
postfix_expr = input("Enter a postfix expression: ")
infix_expr = postfix_to_infix(postfix_expr)
print("Postfix:", postfix_expr)
print("Infix:", infix_expr)
