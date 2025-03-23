#Brute force Method-->Tc: O(n^2)
arr=list(map(int,input("Enter array elements:").split()))
res=[]
for val in arr:
    if val not in res:
        res.append(val)
print(res)
#Better Approach-->using set()-->TC:O(n)
a=list(set(arr))
print(a)

#Optimal Approach-->TC: O(N)
def removeDup(arr):
    i=0
    for j in range(1,len(arr)):
        if(arr[i] != arr[j]):
            i += 1
            arr[i] = arr[j]
    return i+1
index=removeDup(arr)
print(arr[0:index])

