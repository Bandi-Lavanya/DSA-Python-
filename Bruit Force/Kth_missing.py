def kth(arr,k):
    for i in range(0,len(arr)):
        if(arr[i] < k):
            k+=1
        else:
            break
    return k
print(kth([2,3,4,7,11],5))
