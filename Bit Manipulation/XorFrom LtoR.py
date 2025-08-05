#Find xor of numbers from L to R
'''6
The XOR of numbers from 1 to R is: 7
6
The XOR of numbers from 1 to R is: 7'''
def calculate_brute(r):
    xor = 0
    for i in range(1, r+1):
        xor = xor ^ i
    return xor

r = int(input())
print("The XOR of numbers from 1 to R is:", calculate_brute(r))

def calculate_optimized(r):
    if r % 4 == 0:
        return r
    elif r % 4 == 1:
        return 1
    elif r % 4 == 2:
        return r + 1
    else:  # r % 4 == 3
        return 0
r = int(input())
print("The XOR of numbers from 1 to R is:", calculate_optimized(r))