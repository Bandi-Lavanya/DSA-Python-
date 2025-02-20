'''Enter list of elements: 3 1 2 3 3 3 3
Enter the target element: 2
The element is at index: 2'''

def rotated(arr,target):
    s,e=0,len(arr)-1
    while(s<=e):
        mid=(s+e)//2
        if(arr[mid]==target):
            return mid
        if(arr[s]==arr[mid] ==arr[e]):
            s=s+1
            e=e-1
        #if left half is sorted
        elif(arr[s]<=arr[mid]):
            if(arr[s]<= target and target <=arr[mid]):
                e=mid-1
            else:
                s=mid+1
        #if right half is sorted
        else:
            if(arr[mid]<= target and target <=arr[e]):
                s=mid+1
            else:
                e=mid-1
    return -1
arr = list(map(int, input("Enter list of elements: ").split()))
target = int(input("Enter the target element: "))
print("The element is at index:", rotated(arr, target))
