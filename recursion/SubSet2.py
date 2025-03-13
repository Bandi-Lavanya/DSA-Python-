def uniqueSubSets(arr,subset=None, index=0,result=None):
    if result==None:
        result=[]
    if subset==None:
        subset=[]

    if(index==len(arr)):
        result.append(subset[:])
        return result
    # Include the current element
    subset.append(arr[index])
    uniqueSubSets(arr,subset,index+1,result)
    subset.pop()
    #Skip duplicates:
    while index+1 < len(arr) and arr[index] == arr[index+1]:
        index += 1
    # Exclude the current element
    uniqueSubSets(arr,subset,index+1,result)
    return result
arr=list(map(int,input("Enter list elements:").split()))
print(sorted(uniqueSubSets(arr)))
