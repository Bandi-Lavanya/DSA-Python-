# 1 to n
def fun(i,n):
    if(i>n):
        return
    print(i)
    return fun(i+1,n)
fun(1,5)
#n to 1
def fun2(i,n):
    if(i<n):
        return
    print(i)
    return fun2(i-1,n)
fun2(5,1)

#Sum of first N Natural Numbers
def fun3(i,sum):
    if(i < 1):
        return sum
    return fun3(i-1,sum+i)
print(fun3(5,0))
    
'''Using formula to calculate the sum of n numbers
def fromula(n):
    print(n*(n+1)/2)'''

#Factorial of n
def fact(i,f,n):
    if(i>n):
        return f
    f=f*n
    return fact(i,f,n-1)
print(fact(1,1,5))

'''def fact(n):
    if n==0:
       return 1
    return n * fact(n-1)
    '''
