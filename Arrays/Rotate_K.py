def rotateright(arr, k):
    n=len(arr)
    if n == 0:
        return
    k = k % n  # Handle cases where k > n
    if k > n:
        return
    temp = arr[-k:]  # Store the last k elements
    for i in range(n - k - 1, -1, -1):  # Shift remaining elements to the right
        arr[i + k] = arr[i]
    
    for i in range(k):  # Place the stored elements at the beginning
        arr[i] = temp[i]
    return arr
arr=list(map(int,input("Enter array elements:").split()))    
k=int(input("Enter K value:"))    
print(rotateright(arr,k))


def rotateleft(arr1, k):
    n=len(arr1)
    if n == 0:
        return
    k = k % n  # Handle cases where k > n

    temp = arr1[:k]  # Store the first k elements
    for i in range(k, n):  # Shift remaining elements to the left
        arr1[i - k] = arr1[i]
    
    for i in range(n - k, n):  # Place stored elements at the end
        arr1[i] = temp[i - (n - k)]
    return arr1
arr1=list(map(int,input("Enter array elements:").split()))
k=int(input("Enter K value:"))    
print(rotateleft(arr1,k))
'''Enter array elements:1 2 3 4 5
Enter K value:2
[4, 5, 1, 2, 3]
Enter array elements:1 2 3 4 5
Enter K value:2
[3, 4, 5, 1, 2]'''