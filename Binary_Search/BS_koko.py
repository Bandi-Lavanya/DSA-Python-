import math
def findMax(m):
    maxm=0
    for i in range(len(m)):
        maxm=max(maxm,m[i])
    return maxm
def Totalhours(m,hours):
    totalH = 0
    for i in range(len(m)):
        totalH += math.ceil(m[i]/hours)
    return totalH
def koko(m,h):
    low,high= 1, findMax(m)
    while(low<=high):
        mid=(low+high)//2
        totalH=Totalhours(m,mid)
        if(totalH <= h):
            high=mid-1
        else:
            low=mid+1
    return low
m=list(map(int,input("Enter plies of bananas:").split()))
h=int(input("Enter number of hours:"))
print("Koko should eat at least", koko(m,h), "bananas/hr.")
