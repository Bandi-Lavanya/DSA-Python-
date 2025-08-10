def power_brute(x, n):
    result = 1
    for _ in range(n):
        result *= x
    return result

# Example
print(power_brute(2, 5))  # 32

def power_recursive(x, n):
    if n == 0:
        return 1
    half = power_recursive(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return x * half * half

print(power_recursive(2, 5))  # 32


def power_iterative(x, n):
    result = 1
    while n > 0:
        if n % 2 == 1:   # If odd exponent
            result *= x
        x *= x           # Square base
        n //= 2          # Halve exponent
    return result

print(power_iterative(2, 5))  # 32
