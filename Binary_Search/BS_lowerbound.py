#arr[mid] >= target, here s,e are low ,high
#Enter sorted array:1 2 3 3 3 4
#The lowest bound index of target : 2
'''Enter sorted array:1 2 4 6 7
The lowest bound index of target : 2'''
def binary_search(arr,target):
    s,e=0,len(arr)-1
    ans=-1
    while(s<=e):
      mid=(s+e)//2
      if(arr[mid] >= target):
        ans=mid
        e=mid-1
      else:
        s=mid+1
    return ans
arr=list(map(int,input("Enter sorted array:").split()))
print("The lowest bound index of target :",binary_search(arr,3))