def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while i <= high - 1 and arr[i] <= pivot:
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort_helper(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        quick_sort_helper(arr, low, p_index - 1)
        quick_sort_helper(arr, p_index + 1, high)

def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

if __name__ == "__main__":
    arr = [4, 6, 2, 5, 7, 9, 1, 3]
    print("Before Quick Sort:", arr)
    sorted_arr = quick_sort(arr)
    print("After Quick Sort:", sorted_arr)
