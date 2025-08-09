'''Enter a number to find its prime factors: 84
[2, 2, 3, 7]'''
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def prime_factors_brute(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            while n % i == 0:
                factors.append(i)
                n //= i
    return factors
n=int(input("Enter a number to find its prime factors: "))
print(prime_factors_brute(n))  # Example usage, e.g., n = 84

def prime_factors_better(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2

    if n > 2:
        factors.append(n)

    return factors
n=int(input("Enter a number to find its prime factors: "))
print(prime_factors_better(n))  # Example usage, e.g., n = 84
import math

def prime_factors_with_for(N):
    factors = []
    for i in range(2, int(math.isqrt(N)) + 1):
        while N % i == 0:
            factors.append(i)
            N //= i
    if N > 1:
        factors.append(N)
    return factors

# Example usage
print(prime_factors_with_for(84))  # Output: [2, 2, 3, 7]
