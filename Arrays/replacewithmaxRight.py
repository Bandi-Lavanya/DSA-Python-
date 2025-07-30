# Version 1: Brute-force (O(n^2)) — works fine
l = list(map(int, input("Enter list: ").split()))

def ReplaceWithMaxRight(l):
    n = len(l)
    for i in range(n):
        if i == n - 1:
            l[i] = -1
        else:
            m = max(l[i+1:])  # fixed slicing: no need for n+1
            l[i] = m
    return l

print("Output using brute-force method:")
print(ReplaceWithMaxRight(l))

# Version 2: Optimal (O(n)) — fixed function signature (removed 'self')
l = list(map(int, input("Enter list again: ").split()))

def replaceElements(arr):
    n = len(arr)
    rmax = -1
    for i in range(n - 1, -1, -1):
        temp = arr[i]
        arr[i] = rmax
        rmax = max(rmax, temp)
    return arr

print("Output using optimal method:")
print(replaceElements(l))

'''Enter list: 5 4 3 2 1
Output using brute-force method:
[4, 3, 2, 1, -1]
Enter list again: 5 4 3 2 1
Output using optimal method:
[4, 3, 2, 1, -1]'''