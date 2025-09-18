'''Enter the string: (*))
Valid parenthesis string
Enter the string: (*))
Valid parenthesis string'''
class Solution:

    # Recursive function to check if the parenthesis string is valid
    def isValid(self, s, index, open_count):

        # If open parentheses count becomes negative, it's invalid
        if open_count < 0:
            return False

        # If we reach the end of the string, check if all opens are closed
        if index == len(s):
            return open_count == 0

        # Get the current character
        c = s[index]

        # If it's an opening bracket '(', increase open count
        if c == '(':
            return self.isValid(s, index + 1, open_count + 1)

        # If it's a closing bracket ')', decrease open count
        elif c == ')':
            return self.isValid(s, index + 1, open_count - 1)

        # If it's '*', try all three options:
        # 1. Treat '*' as empty string
        # 2. Treat '*' as '('
        # 3. Treat '*' as ')'
        else:
            return (self.isValid(s, index + 1, open_count) or
                    self.isValid(s, index + 1, open_count + 1) or
                    self.isValid(s, index + 1, open_count - 1))

# Driver code
if __name__ == "__main__":
    # Prompt the user for input
    s = input("Enter the string: ")

    # Create Solution object and call the recursive function
    sol = Solution()
    if sol.isValid(s, 0, 0):
        print("Valid parenthesis string")
    else:
        print("Invalid parenthesis string")
#Optimal Approach
class Solution:

    # Function to check if the string is valid using greedy logic
    def checkValidString(self, s: str) -> bool:

        # Variable to store minimum number of open brackets possible
        min_open = 0

        # Variable to store maximum number of open brackets possible
        max_open = 0

        # Traverse each character in the string
        for char in s:

            # If current character is '('
            if char == '(':
                min_open += 1
                max_open += 1

            # If current character is ')'
            elif char == ')':
                min_open -= 1
                max_open -= 1

            # If current character is '*', it can be '(', ')' or ''
            else:
                 # If '*' acts as ')'
                min_open -= 1    
                # If '*' acts as '('
                max_open += 1      

            # If max_open goes below 0, we have too many unmatched ')'
            if max_open < 0:
                return False

            # min_open should not be negative
            if min_open < 0:
                min_open = 0

        # At the end, all opens must be matched for valid string
        return min_open == 0


# Driver code
if __name__ == "__main__":
    s = input("Enter the string: ")
    sol = Solution()
    if sol.checkValidString(s):
        print("Valid parenthesis string")
    else:
        print("Invalid parenthesis string")