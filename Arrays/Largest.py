arr=list(map(int,input("Enter array elements:").split()))
arr.sort()
print("The Largest element in the array is:",arr[len(arr)-1])# or arr[-1]

#Using recursions
max=arr[0]
for i in range(len(arr)):
    if(arr[i]> max):
        max=arr[i]
print(max)

