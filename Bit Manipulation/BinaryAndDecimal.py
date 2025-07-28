'''Enter a decimal number:13
The binary Number: 1101
Enter a binary number: 1101
The decimal number is: 13'''
#Decimal to Binary Convertion 
n=int(input("Enter a decimal number:"))
res=""
if n==0:
    print(0)
while n!=1:
    res+=str(n%2)
    n=n//2
res+='1'
print("The binary Number:",res[::-1])

#Binary to decimal:
n = input("Enter a binary number: ")
d = 0
for i in range(len(n)):
    d += int(n[i]) * (2 ** (len(n) - 1 - i))
print("The decimal number is:",d)
