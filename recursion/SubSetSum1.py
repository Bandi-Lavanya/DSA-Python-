'''brute force method

from itertools import combinations
def SubSetSum(arr):
    sums=set()
    for i in range(len(arr)):
        for subset in combinations(arr,i):
            sums.add(sum(subset))

    return sorted(sums)
arr=list(map(int,input("Enter list elements:").split()))
print(SubSetSum(arr))'''

# Optimal Approach

def SubSetSum(arr, index=0,currSum=0,result=None):
    if result==None:
        result=[]
    if(index==len(arr)):
        result.append(currSum)
        return result
    # Include the current element
    SubSetSum(arr,index+1,currSum+arr[index],result)
    # Exclude the current element
    SubSetSum(arr,index+1,currSum,result)
    return result
arr=list(map(int,input("Enter list elements:").split()))
print(sorted(SubSetSum(arr)))
