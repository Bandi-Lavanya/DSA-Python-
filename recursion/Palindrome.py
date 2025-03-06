import re
def palindrome(i,s):
    if(i>=len(s)):
        return True
    if(s[i]!=s[len(s)-(i+1)]):
        return False
    return palindrome(i+1,s)
s=input("Enter a string:")
s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#s = "".join(filter(str.isalnum, s)).lower()
print(palindrome(0,s))    