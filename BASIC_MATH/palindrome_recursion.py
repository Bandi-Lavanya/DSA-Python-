def palindrome(m,s=0,e=None):
    if e is None:
        e=len(m)-1
    if(s>=e):
        return True
    elif(m[s] != m[e]):
        return False
    else:
        return palindrome(m,s+1,e-1)
m=(input("Enter a string:"))
print(palindrome(m))