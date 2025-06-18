#Length of the longest subarray with zero Sum

def solve_brute(a):
    maxx = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum == 0:
                maxx = max(maxx, j-i+1)
    return maxx

a = [9, -3, 3, -1, 6, -5]
print(solve_brute(a))




def maxLen_optimal(A, n):
    mpp = {}
    maxi = 0
    sum = 0
    for i in range(n):
        sum += A[i]
        if sum == 0:
            maxi = i + 1
        else:
            if sum in mpp:
                maxi = max(maxi, i - mpp[sum])
            else:
                mpp[sum] = i
    return maxi
a = [9, -3, 3, -1, 6, -5]
print(maxLen_optimal(a, len(a)))




