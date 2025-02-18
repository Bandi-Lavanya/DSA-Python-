def binary_search(arr,target):
    s,e=0,len(arr)-1
    while(s<=e):
      mid=(s+e)//2
      if(arr[mid] == target):
        return mid
      elif(target > arr[mid]):
        s=mid+1
      else:
        e=mid-1
    return s
        
arr=list(map(int,input("Enter sorted array:").split()))
print("The target is in index number:",binary_search(arr,4))