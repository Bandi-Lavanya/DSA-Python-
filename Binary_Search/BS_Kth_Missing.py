def missingK(arr, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1
n = int(input("Enter size a array:"))
arr=list(map(int,input("Enter sorted array:").split()))
k = int(input("Enter K:"))
ans = missingK(arr, n, k)
print("The missing number is:", ans)


