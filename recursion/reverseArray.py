def reverse(i,a,t):
    if(i<0):
        return t
    t.append(a[i])
    return reverse(i-1,a,t)
a=list(map(int,input("Enter list elements:").split()))
t=[]
print(reverse(len(a)-1,a,t))

      
    