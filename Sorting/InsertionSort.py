def insertion_sort(arr, n):
    for i in range(n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]  # Swap
            j -= 1
    print("After insertion sort:")
    print(*arr)

arr = [13, 46, 24, 52, 20, 9]
n = len(arr)
print("Before Using insertion Sort:")
print(*arr)
insertion_sort(arr, n)
