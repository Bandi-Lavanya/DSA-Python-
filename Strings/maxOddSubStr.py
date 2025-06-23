def largestOddNumber_brute(num):
    l=""
    for i in range(len(num)):
        for j in range(i+1,len(num)+1):
            temp=num[i:j]
            if(int(temp)%2 != 0):
                if(l==""):
                    l=int(temp)
                else:
                    l=max(l,int(temp))
    return str(l)
def largestOddNumber_optimal(num):   
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                return num[:i+1]
        return ""


s="354726"
print(largestOddNumber_brute(s))
print(largestOddNumber_optimal(s))