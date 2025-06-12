def max_subarray_sum_brute(arr, n):
    maxi = float('-inf')  # Equivalent to Integer.MIN_VALUE

    for i in range(n):
        for j in range(i, n):
            total = 0
            for k in range(i, j + 1):
                total += arr[k]
            maxi = max(maxi, total)

    return maxi

def max_subarray_sum_better(arr, n):
    maxi = float('-inf')  # Initialize with the smallest possible number

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]  # Sum of subarray arr[i..j]
            maxi = max(maxi, total)  # Track maximum sum

    return maxi

def max_subarray_sum_optimal(arr, n):
    maxi = float('-inf')  # Initialize to negative infinity
    total = 0

    for i in range(n):
        total += arr[i]
        if total > maxi:
            maxi = total
        if total < 0:
            total = 0

    # To consider the sum of the empty subarray, uncomment this:
    # if maxi < 0:
    #     maxi = 0

    return maxi

def maxSubarraySum(arr, n):
    maxi = float('-inf')  # maximum sum
    sum = 0

    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(n):

        if sum == 0:
            start = i  # starting index

        sum += arr[i]

        if sum > maxi:
            maxi = sum

            ansStart = start
            ansEnd = i

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0

    # printing the subarray:
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=" ")
    print("]")


# Example usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
max_sum1 = max_subarray_sum_brute(arr, n)
print("The maximum subarray sum is:", max_sum1)
max_sum2 = max_subarray_sum_better(arr, n)
print("The maximum subarray sum is:", max_sum2)
max_sum3 = max_subarray_sum_optimal(arr, n)
print("The maximum subarray sum is:", max_sum3)
maxSubarraySum(arr,n)