'''Enter list of elements: 7 8 9 1 2 3 4 5 6
Enter the target element: 1
The element is at index: 3'''

def rotated(arr,target):
    s,e=0,len(arr)-1
    while(s<=e):
        mid=(s+e)//2
        #if left half is sorted
        if(arr[mid]==target):
            return mid
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
