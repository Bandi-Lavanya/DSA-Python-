#Brute Force --> TC:O(N^2)
arr=list(map(int,input("Enter the array elements:").split()))
n=len(arr)
temp=True
for i in range(n):
    for j in range(i+1,n):
        if(arr[j]<arr[i]):
            temp=False
print(temp)

#Optimal Approach
def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True
print("The Array is sorted?",isSorted(arr,n))
    