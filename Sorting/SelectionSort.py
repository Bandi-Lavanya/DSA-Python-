'''Before selection sort:
13 46 24 52 20 9
After selection sort:
9 13 20 24 46 52'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        # Swap
        arr[mini], arr[i] = arr[i], arr[mini]
    print("After selection sort:")
    print(*arr)
    # with *arr-->9 13 20 24 46 52 without *arr-->[9, 13, 20, 24, 46, 52]

arr = [13, 46, 24, 52, 20, 9]
print("Before selection sort:")
print(*arr)
selection_sort(arr)
