#Brute Force Approach
arr=list(map(int,input("Enter the Array elements:").split()))
n=len(arr)
if n==1 or n==1:
    print(-1,-1)
arr.sort()
small=arr[1]
large=arr[n-2]
print("Second Smallest is:",small)
print("Second largest is:",large)

#Better approach--> TC:O(N)
def BetterApproach(arr,n):
    if n==1 or n==1:
        print(-1,-1)
    small=float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print("Second smallest is", second_small)
    print("Second largest is", second_large)
n=len(arr)
BetterApproach(arr,n)


#Optimal approach--> TC:O(N)
def secondSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    print("The Second Smallest:", second_small)


def secondLargest(arr, n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    print("The Second Smallest:", second_large)
secondSmallest(arr,n)
secondLargest(arr,n)








