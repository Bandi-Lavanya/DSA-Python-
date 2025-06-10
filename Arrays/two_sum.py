def two_sum_brute(n, arr, target):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return "YES"
    return "NO"



def two_sum_better(n, arr, target):
    mpp = {}  # value -> index
    for i in range(n):
        num = arr[i]
        more_needed = target - num
        if more_needed in mpp:
            return [mpp[more_needed], i]  # Return the indices
        mpp[num] = i
    return []  # Return an empty list if no such pair is found



def two_sum_optimal(n, arr, target):
    arr.sort()
    left, right = 0, n - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return "YES"
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return "NO"


# Example usage
n = 5
arr = [2, 6, 5, 8, 11]
target = 14
ans1 = two_sum_brute(n, arr, target)
print("This is the answer ", ans1)
ans2 = two_sum_better(n, arr, target)
if ans2:
    print("Indices of the elements that sum to target:", ans2)
else:
    print("No two elements found that sum to the target.")
ans3 = two_sum_optimal(n, arr, target)
print("This is the answer", ans3)
