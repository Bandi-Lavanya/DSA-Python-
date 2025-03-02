def merge(arr, low, mid, high):
    temp = []  # Temporary array
    left = low  # Starting index of left half
    right = mid + 1  # Starting index of right half
    # Merging elements in sorted order
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    # If elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    # If elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1
    
    # Transferring all elements from temporary to original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)  # Left half
    merge_sort(arr, mid + 1, high)  # Right half
    merge(arr, low, mid, high)  # Merging sorted halves

arr = [9, 4, 7, 6, 3, 1, 5]
print("Before sorting array:", arr)
merge_sort(arr, 0, len(arr) - 1)
print("After sorting array:", arr)


'''Before sorting array: [9, 4, 7, 6, 3, 1, 5]
After sorting array: [1, 3, 4, 5, 6, 7, 9]'''
