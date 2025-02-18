def binary_search(num):
    if(num==0 or num==1):
      return num
    s,e=0,num
    ans=0
    while(s<=e):
      mid=(s+e)//2
      if(mid * mid == num):
        return mid
      elif(mid * mid < num):
        s=mid+1
        ans=mid
      else:
        e=mid-1
    return ans
num=int(input("Enter a number:"))
print("The square root of number is:",binary_search(num))