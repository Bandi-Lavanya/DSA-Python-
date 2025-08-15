'''Enter an infix expression: (A-B/C)*(A/K-L)
Infix: (A-B/C)*(A/K-L)
Prefix: *-A/BC-/AKL'''
# Function to check operator precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

# Function to check if character is an operator
def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

# Function to convert infix to prefix
def infix_to_prefix(expression):
    # Step 1: Reverse the infix expression
    expression = expression[::-1]
    
    # Step 2: Swap '(' with ')' and vice versa
    swapped = ""
    for char in expression:
        if char == '(':
            swapped += ')'
        elif char == ')':
            swapped += '('
        else:
            swapped += char
    
    # Step 3: Convert the modified expression to postfix
    stack = []
    postfix = ""
    for char in swapped:
        if char.isalnum():  # Operand
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:  # Operator
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix += stack.pop()
            stack.append(char)

    while stack:
        postfix += stack.pop()

    # Step 4: Reverse postfix to get prefix
    return postfix[::-1]

# Example usage
expr = input("Enter an infix expression: ")
prefix = infix_to_prefix(expr)
print("Infix:", expr)
print("Prefix:", prefix)
