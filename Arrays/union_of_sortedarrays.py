def find_union_bruit(arr1, arr2):
    freq = {}
    union = []
    
    for num in arr1:
        freq[num] = freq.get(num, 0) + 1
        #It either initializes the count of num to 1 (if it’s not there yet) or it increments the existing count by 1 (if it's already in the dictionary).
    for num in arr2:
        freq[num] = freq.get(num, 0) + 1
    
    for num in freq:
        union.append(num)
    
    return union

def find_union_better(arr1, arr2):
    s = set()
    union = []
    
    for num in arr1:
        s.add(num)
    
    for num in arr2:
        s.add(num)
    
    for num in s:
        union.append(num)
    
    return union


def find_union_optimal(arr1, arr2):
    i, j = 0, 0  # Pointers
    union = []  # Union list

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:  # Case 1 and 2
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:  # Case 3
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

    while i < len(arr1):  # If any elements left in arr1
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1

    while j < len(arr2):  # If any elements left in arr2
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    return union



arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

union1 = find_union_bruit(arr1, arr2)
union2 = find_union_better(arr1, arr2)
union3 = find_union_optimal(arr1, arr2)

print(*union1)
print(*union2)
print(*union3)
