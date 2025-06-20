#Merge two Sorted Arrays Without Extra Space
def merge_brute(arr1, arr2, n, m):

    # Declare a 3rd array and 2 pointers:
    arr3 = [0] * (n + m)
    left = 0
    right = 0
    index = 0

    # Insert the elements from the 2 arrays
    # into the 3rd array using left and right
    # pointers:
    while left < n and right < m:
        if arr1[left] <= arr2[right]:
            arr3[index] = arr1[left]
            left += 1
            index += 1
        else:
            arr3[index] = arr2[right]
            right += 1
            index += 1

    # If right pointer reaches the end:
    while left < n:
        arr3[index] = arr1[left]
        left += 1
        index += 1

    # If left pointer reaches the end:
    while right < m:
        arr3[index] = arr2[right]
        right += 1
        index += 1

    # Fill back the elements from arr3[]
    # to arr1[] and arr2[]:
    for i in range(n + m):
        if i < n:
            arr1[i] = arr3[i]
        else:
            arr2[i - n] = arr3[i]

arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
n = 4
m = 3
merge_brute(arr1, arr2, n, m)

print("The merged arrays are:")
print("arr1[] = ", end="")
for i in range(n):
    print(arr1[i], end=" ")
print("\narr2[] = ", end="")
for i in range(m):
    print(arr2[i], end=" ")
print() 




def merge_optimal1(arr1, arr2, n, m):

    # Declare 2 pointers:
    left = n - 1
    right = 0

    # Swap the elements until arr1[left] is smaller than arr2[right]:
    while left >= 0 and right < m:
        if arr1[left] > arr2[right]:
            arr1[left], arr2[right] = arr2[right], arr1[left]
            left -= 1
            right += 1
        else:
            break

    # Sort arr1[] and arr2[] individually:
    arr1.sort()
    arr2.sort()


arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
n = 4
m = 3
merge_optimal1(arr1, arr2, n, m)
print("The merged arrays are:")
print("arr1[] = ", end="")
for i in range(n):
    print(arr1[i], end=" ")
print("\narr2[] = ", end="")
for i in range(m):
    print(arr2[i], end=" ")
print()



#Optimal Solution -2
def swapIfGreater(arr1, arr2, ind1, ind2):
    if arr1[ind1] > arr2[ind2]:
        arr1[ind1], arr2[ind2] = arr2[ind2], arr1[ind1]

def merge(arr1, arr2, n, m):
    # len of the imaginary single array:
    len = n + m

    # Initial gap:
    gap = (len // 2) + (len % 2)

    while gap > 0:
        # Place 2 pointers:
        left = 0
        right = left + gap
        while right < len:
            # case 1: left in arr1[]
            # and right in arr2[]:
            if left < n and right >= n:
                swapIfGreater(arr1, arr2, left, right - n)
            # case 2: both pointers in arr2[]:
            elif left >= n:
                swapIfGreater(arr2, arr2, left - n, right - n)
            # case 3: both pointers in arr1[]:
            else:
                swapIfGreater(arr1, arr1, left, right)
            left += 1
            right += 1
        # break if iteration gap=1 is completed:
        if gap == 1:
            break
        # Otherwise, calculate new gap:
        gap = (gap // 2) + (gap % 2)

arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]
n = 4
m = 3
merge_optimal1(arr1, arr2, n, m)
print("The merged arrays are:")
print("arr1[] = ", end="")
for i in range(n):
    print(arr1[i], end=" ")
print("\narr2[] = ", end="")
for i in range(m):
    print(arr2[i], end=" ")
print()


