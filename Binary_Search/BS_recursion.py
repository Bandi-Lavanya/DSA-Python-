def binary_search(arr,s,e,target):
    if(s>e):
      return -1
    mid=(s+e)//2
    if(arr[mid] == target):
      return mid
    elif(target > arr[mid]):
      return binary_search(arr,mid+1,e,target)
    else:
      return binary_search(arr,s,mid-1,target)
arr=list(map(int,input("Enter sorted array:").split()))
print("The target is in index number:",binary_search(arr,0,len(arr)-1,4))
