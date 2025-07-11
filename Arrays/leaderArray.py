def printLeadersBruteForce(arr, n):
    ans = []
  
    for i in range(n):
        leader = True

        # Checking whether arr[i] is greater than all 
        # the elements in its right side
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                # If any element found is greater than current leader,
                # curr element is not the leader.
                leader = False
                break

        # Push all the leaders in ans array.
        if leader:
            ans.append(arr[i])

    return ans

def printLeaders_optimal(arr, n):
    ans = []
  
    # Last element of an array is always a leader,
    # push into ans array.
    max_elem = arr[n - 1]
    ans.append(arr[n - 1])

    # Start checking from the end whether a number is greater
    # than max no. from right, hence leader.
    for i in range(n - 2, -1, -1):
        if arr[i] > max_elem:
            ans.append(arr[i])
            max_elem = arr[i]

    return ans


n = 6
arr = [10, 22, 12, 3, 0, 6]
ans = printLeadersBruteForce(arr, n)
print(*ans)
ans1 = printLeaders_optimal(arr, n)
for i in range(len(ans1)-1, -1, -1):
        print(ans1[i], end=" ")
print()


