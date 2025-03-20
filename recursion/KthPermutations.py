def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def get_permutation(n, k):
    numbers = list(range(1, n + 1))  # List of available numbers
    k -= 1  # Convert to 0-based index
    result = ""
    
    for i in range(n, 0, -1):
        fact = factorial(i - 1)  # Compute factorial of (i-1)
        index = k // fact  # Determine the index of the next number
        result += str(numbers[index])  # Append the selected number
        numbers.pop(index)  # Remove the used number
        k %= fact  # Update k

    return result

# Example usage
n, k = 3, 3
ans = get_permutation(n, k)
print("The Kth permutation sequence is", ans)


'''from itertools import permutations

def get_permutation(n, k):
    s = "".join(str(i) for i in range(1, n + 1))
    res = sorted("".join(p) for p in permutations(s))
    return res[k - 1]

# Example usage
n, k = 3, 3
ans = get_permutation(n, k)
print("The Kth permutation sequence is", ans)
'''


'''def swap(s, i, j):
    s[i], s[j] = s[j], s[i]

def permutation_helper(s, index, res):
    if index == len(s):
        res.append("".join(s))  # Convert list to string and add to result
        return

    for i in range(index, len(s)):
        swap(s, i, index)  # Swap characters
        permutation_helper(s, index + 1, res)  # Recur for next index
        swap(s, i, index)  # Backtrack

def get_permutation(n, k):
    s = [str(i) for i in range(1, n + 1)]  # Create a list of numbers as strings
    res = []
    permutation_helper(s, 0, res)  # Generate all permutations
    res.sort()  # Sort the permutations lexicographically
    return res[k - 1]  # Return the Kth permutation (1-based index)

# Example usage
n, k = 3, 3
ans = get_permutation(n, k)
print("The Kth permutation sequence is", ans)
'''