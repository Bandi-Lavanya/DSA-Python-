'''Enter a number to find its prime factors: 3
[3]
Enter a number to find its prime factors: 12   
[2, 2, 3]
Enter a number to find its prime factors: 16   
[2, 2, 2, 2]
Enter a number:60
2 2 3 5'''
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
n=int(input("Enter a number to find its prime factors: "))
# Example usage
print(prime_factors_with_for(n))  # Output: [2, 2, 3, 7]


# Optimal for multiple queries
import math

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return [p for p in range(2, limit + 1) if is_prime[p]]

def prime_factors(n, primes):
    factors = []
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors

# Example usage
n = int(input("Enter a number:").strip())
primes = sieve(int(math.sqrt(n)) + 1)
print(" ".join(map(str, prime_factors(n, primes))))
