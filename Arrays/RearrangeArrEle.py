def rearrange_by_sign_brute(A):
    # Define 2 lists, one for storing positive and other for negative elements of the array.
    pos = []
    neg = []
  
    # Segregate the array into positives and negatives.
    for i in range(len(A)):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])
  
    # Positives on even indices, negatives on odd.
    for i in range(len(pos)):
        A[2 * i] = pos[i]
    for i in range(len(neg)):
        A[2 * i + 1] = neg[i]
  
    return A

def rearrange_by_sign_optimal(arr):
    n = len(arr)
    ans = [0] * n  # Initialize result array with 0s

    pos_index = 0  # Start filling positives at even indices
    neg_index = 1  # Start filling negatives at odd indices

    for num in arr:
        if num < 0:
            ans[neg_index] = num
            neg_index += 2
        else:
            ans[pos_index] = num
            pos_index += 2

    return ans


# Array Initialisation.
A = [1, 2, -4, -5,-6,3]
ans1 = rearrange_by_sign_brute(A)
print(*ans1)
ans2 = rearrange_by_sign_optimal(A)
print(*ans2)