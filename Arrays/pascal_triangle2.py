# This code prints the nth row of Pascal's Triangle.
import math

def nCr_brute(n, r):
    res = 1
    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle_brute(n):
    # printing the entire row n:
    for c in range(1, n+1):
        print(nCr_brute(n-1, c-1), end=" ")
    print()

n = 5
pascalTriangle_brute(n)

def pascalTriangle_optimal(n):
    ans = 1
    print(ans, end=" ") # printing 1st element

    #Printing the rest of the part:
    for i in range(1, n):
        ans = ans * (n - i)
        ans = ans // i
        print(ans, end=" ")
    print()

n = 5
pascalTriangle_optimal(n)
