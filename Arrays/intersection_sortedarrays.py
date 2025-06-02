def intersection_bruit(arr1,arr2):
    vis = [0] * len(arr2)  # Mark visited elements in arr2
    res=[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j] and vis[j]==0:
                res.append(arr1[i])
                vis[j]=1
                break
            if(arr2[j]> arr1[i]):
                break
    return res

def intersection_optimal(arr1,arr2):
    res1=[]
    i,j=0,0
    while(i<len(arr1) and j<len(arr2)):
        if arr1[i]<arr2[j]:
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            res1.append(arr1[i])
            i+=1
            j+=1
    return res1
        
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

res= intersection_bruit(arr1, arr2)
print(*res)
res1= intersection_optimal(arr1, arr2)
print(*res1)


