def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

    print("After bubble sort:")
    print(*arr)
arr = [13, 46, 24, 52, 20, 9]
print("Before Using Bubble Sort:")
print(*arr)
bubble_sort(arr)
