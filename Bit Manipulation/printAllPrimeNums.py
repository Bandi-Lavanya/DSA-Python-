'''10
[2, 3, 5, 7]'''
# Brute force: check divisibility by all smaller numbers
def primes_brute(N):
    primes = []
    for x in range(2, N + 1):
        is_prime = True
        for d in range(2, x):          # try every possible divisor
            if x % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes

# Example usage:
N = int(input().strip())
print(primes_brute(N))


import math

def primes_better(N):
    if N < 2:
        return []
    primes = [2] if N >= 2 else []
    for x in range(3, N + 1, 2):            # only odd candidates
        limit = math.isqrt(x)
        is_prime = True
        for d in range(3, limit + 1, 2):   # only odd divisors
            if x % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(x)
    return primes

# Example usage:
N = int(input().strip())
print(primes_better(N))


import math

def primes_sieve(N):
    if N < 2:
        return []
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    limit = math.isqrt(N)
    for p in range(2, limit + 1):
        if is_prime[p]:
            # start from p*p, step p
            for multiple in range(p * p, N + 1, p):
                is_prime[multiple] = False
    return [i for i, val in enumerate(is_prime) if val]

# Example usage:
N = int(input().strip())
print(primes_sieve(N))
