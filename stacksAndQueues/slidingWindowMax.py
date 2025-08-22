def get_max(arr, l, r):
    maxi = float("-inf")
    for i in range(l, r + 1):
        maxi = max(maxi, arr[i])
    return maxi

def max_sliding_window(arr, k):
    left = 0
    right = 0
    maxx = []

    # Move right pointer to the first (k-1) position
    right =k-1

    # Now slide the window
    while right < len(arr):
        maxx.append(get_max(arr, left, right))
        left += 1
        right += 1

    return maxx


# Driver code
arr = [4, 0, -1, 3, 5, 3, 6, 8]
k = 3
ans = max_sliding_window(arr, k)

print(f"Maximum element in every {k} window: ")
print(ans)


from collections import deque

def maxSlidingWindow(nums, k):
    n = len(nums)
    result = []
    q = deque()  # stores indices, not values

    for i in range(n):
        # Remove elements out of the current window
        if q and q[0] == i - k:
            q.popleft()

        # Remove smaller elements (they are useless since current num is larger)
        while q and nums[q[-1]] < nums[i]:
            q.pop()

        # Add current element’s index
        q.append(i)

        # If window size reached, record max (front of deque)
        if i >= k - 1:
            result.append(nums[q[0]])

    return result


# Driver Code
arr = [1,3,-1,-3,5,3,7,1,6]
k = 3
ans = maxSlidingWindow(arr, k)

print("Maximum element in every", k, "window:")
print(ans)
