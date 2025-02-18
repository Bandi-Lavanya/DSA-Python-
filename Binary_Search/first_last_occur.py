def firstlast(arr,target):
    first=-1
    last=-1
    for i in range(len(arr)):
        if arr[i]==target:
            if first ==-1:
                first=i
            last=i
    return [first,last]
arr=list(map(int,input("Enter list of elements:").split()))
print("The first and lastbound:", firstlast(arr,5))