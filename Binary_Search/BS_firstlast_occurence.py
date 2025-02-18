def find_first(arr, target):
    low, high = 0, len(arr) - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1  # Move left to find the first occurrence
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return first

def find_last(arr, target):
    low, high = 0, len(arr) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1  # Move right to find the last occurrence
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return last

def firstlast(arr, target):
    return [find_first(arr, target), find_last(arr, target)]

arr = list(map(int, input("Enter a sorted list of elements: ").split()))
target = int(input("Enter the target element: "))
print("The first and last bound:", firstlast(arr, target))
