'''Enter a Number:13(beacuse 13=1101)
Enter the bit position to check:2
True
True

Enter a Number:9(because 9=1001)
Enter the bit position to check:2
False
False'''

n=int(input("Enter a Number:"))
m=int(input("Enter the bit position to check:"))
def is_ith_bit_set_leftshift(n, i):
    # Check if the ith bit is set in the number n using left shift
    return (n & (1 << i)) != 0
def is_ith_bit_set_rightshift(n, i):
    # Check if the ith bit is set in the number n using left shift
    return ((n >> i) & 1) != 0

print(is_ith_bit_set_leftshift(n, m))  
print(is_ith_bit_set_rightshift(n, m)) 


'''Enter a Number:9
Enter the bit position to set:2
13'''
n=int(input("Enter a Number:"))
m=int(input("Enter the bit position to set:"))
def set_ith_bit(n, i):
    # Set the ith bit of n to 1
    return n | (1 << i)
print(set_ith_bit(n, m)) 

'''Enter a Number:13
Enter the bit position to set:2
9'''
def clear_ith_bit(n,m):
    return n & ~(1 << m)
print(clear_ith_bit(n, m))

'''Enter a Number:13
Enter the bit position to set:2
9'''
def toggle_ith_bit(n, m):
    return n ^ (1 << m)
print(toggle_ith_bit(n, m))  # Toggle the ith bit of n

#Remoive the last set bit (rightmost set bit)
'''Enter a Number:12
After removing the last set bit of n we get: 8'''
def remove_last_set_bit(n):
    return n & (n - 1)
n=int(input("Enter a Number:"))
print('After removing the last set bit of n we get:',remove_last_set_bit(n))  # Remove the last set bit of n

#Check if a number is power of 2
'''Enter a Number:16
True'''
def is_power_of_two(n):
    # A number is a power of 2 if it has only one bit set
    return n > 0 and (n & (n - 1)) == 0
n = int(input("Enter a Number:"))
print(is_power_of_two(n))

#Count the number of set bits in a number
'''Enter a Number:13
Number of set bits in 13 : 3
Enter a Number:16
Number of set bits in 16 : 1'''
def count_set_bits1(n):
    count = 0
    while n>1:
        if(n%2==1):
            count += 1
        n = n // 2
    return count + 1 if n == 1 else count
n = int(input("Enter a Number:"))
print("Number of set bits in", n, ":", count_set_bits1(n))
def count_set_bits2(n):
    count = 0
    while n>1:
        count+=n&1
        n = n // 2
    return count + 1 if n == 1 else count
n = int(input("Enter a Number:"))
print("Number of set bits in", n, ":", count_set_bits2(n))
'''Enter a Number:18
Number of set bits in 18 : 2'''
def count_set_bits3(n):
    count = 0
    while n!=0:
        n=n&(n-1)
        count+=1
    return count + 1 if n == 1 else count
n = int(input("Enter a Number:"))
print("Number of set bits in", n, ":", count_set_bits3(n))
