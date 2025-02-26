import math
def SumOfDivisors(arr,div):
    n=len(arr)
    sum=0
    for i in range(n):
        sum +=math.ceil(arr[i]/div)
    return sum

def SmallestDiv(arr,threshold):
    low,high=1,max(arr)
    ans=-1
    while(low <= high):
        mid=(low+high)//2
        if(SumOfDivisors(arr,mid) <= threshold):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

arr=list(map(int,input("Enter list of numbers:").split()))
threshold=int(input("Enter the threshold:"))
print("The smallest divisor is",SmallestDiv(arr,threshold))