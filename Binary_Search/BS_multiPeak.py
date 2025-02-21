'''Enter array elements: 1 2 3 4 5 4 3
The peak element is at index: 4'''

def peakelement(arr):
    n = len(arr)
    # Edge cases for arrays of size 1 or 2
    if n == 1:
        return 0
    if arr[0] > arr[1]:  # Check if first element is a peak
        return 0
    if arr[n-1] > arr[n-2]:  # Check if last element is a peak
        return n-1
    # Binary search for peak element
    low, high = 1, n-2  # Start from the second element to the second last element
    while low <= high:
        mid = (low + high) // 2
        # Check if mid is a peak element
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] > arr[mid-1]:  # Move right
            low = mid + 1
        elif arr[mid] > arr[mid+1]:  # Move left
            high = mid - 1
        else: 
            low=mid+1 # Move right
    return -1  # Return -1 if no peak found (should not happen for valid input)
arr = list(map(int, input("Enter array elements: ").split()))
print("The peak element is at index:", peakelement(arr))
