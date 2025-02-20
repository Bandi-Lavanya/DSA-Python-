'''
import sys
def findMin(arr):
    low = 0
    high = len(arr) - 1
    ans = sys.maxsize

    while low <= high:
        mid = (low + high) // 2
        # search space is already sorted
        # then arr[low] will always be
        # the minimum in that search space:
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break
            
        if arr[low] <= arr[mid]:  # if left part is sorted
            ans = min(ans, arr[low])  # keep the minimum
            low = mid + 1  # eliminate left half

        else:  # if right part is sorted
            ans = min(ans, arr[mid])  # keep the minimum
            high = mid - 1  # eliminate right half

    return ans

arr = list(map(int, input("Enter list of elements: ").split()))
print("The minimum element in the rotated sorted array is:", rotated(arr))'''

def rotated(arr):
    s, e = 0, len(arr) - 1
    while s < e:  
        mid = (s + e) // 2  
        # If the right part is sorted, then min is in left or at mid
        if arr[mid] > arr[e]:  
            s = mid + 1  
        else:  
            e = mid  
    return arr[s]  # The minimum element

arr = list(map(int, input("Enter list of elements: ").split()))
print("The minimum element in the rotated sorted array is:", rotated(arr))

