def min_bit_flips(a, b):
    xor_result = a ^ b
    count = 0
    while xor_result:
        count += xor_result & 1  # check if the last bit is 1
        # or we can use condition if xor_result & 1<<i:
        xor_result >>= 1         # right shift to check the next bit
    return count

# Example usage:
print(min_bit_flips(10, 20))  # Output: 4
