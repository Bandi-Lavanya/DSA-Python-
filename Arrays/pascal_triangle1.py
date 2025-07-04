#given the row number r and the column number c, and we need to find out the element at position (r,c)
import math

def nCr(n, r):
    res = 1

    # calculating nCr:
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)

    return res

def pascalTriangle(r, c):
    element = nCr(r - 1, c - 1)
    return element
r = 5 # row number
c = 3 # col number
element = pascalTriangle(r, c)
print(f"The element at position (r,c) is: {element}")