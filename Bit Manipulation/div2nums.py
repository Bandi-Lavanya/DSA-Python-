#swap two number without using third variable
'''Enter a Number:1
Enter another Number:2
After swapping: n = 2 , m = 1'''
n = int(input("Enter a Number:"))
m = int(input("Enter another Number:"))
n = n ^ m
m= n ^ m
n = n ^ m
print("After swapping: n =", n, ", m =", m)

#divide two numbers without using division and multiplication opertors
'''Enter a Number:22
Enter another Number:7
Result of division: 3'''
def divide_without_division(n, m):
    s=0
    cnt=0
    while(s + m <= n):
        s += m
        cnt += 1
    return cnt

n = int(input("Enter a Number:"))
m = int(input("Enter another Number:"))
print("Result of division:", divide_without_division(n, m))

'''Enter a Number:12
Enter another Number:3
Result of division: 4'''
def divide_without_division2(n, m):
    if m == 0:
        raise ZeroDivisionError("Division by zero is undefined")
    if n == m:
        return 1
    if n == 0:
        return 0

    # Determine the sign of the result
    sign = -1 if (n < 0) ^ (m < 0) else 1

    # Work with absolute values
    n = abs(n)
    m = abs(m)

    result = 0

    while n >= m:
        cnt = 0
        # Find the highest power of 2 such that (m << cnt) <= n
        while n >= (m << (cnt + 1)):
            cnt += 1

        # Subtract the found multiple from n
        n -= (m << cnt)
        # Add the corresponding power of 2 to the result
        result += (1 << cnt)

    return sign * result

n = int(input("Enter a Number:"))
m = int(input("Enter another Number:"))
print("Result of division:", divide_without_division2(n, m))
