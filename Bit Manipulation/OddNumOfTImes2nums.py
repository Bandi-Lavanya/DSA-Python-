'''Enter List elements:4 3 4 4 4 5 3 3 7 3
The number that appears odd number of times:
5 7 The two odd occurring numbers are: (7, 5)''' 
def oddnum_brute(l):
    d={}
    for i in l:
        d[i]= d.get(i, 0) + 1
    for i in d:
        if d[i] % 2 != 0:
            print(i, end=' ')
l=list(map(int,input("Enter List elements:").split()))
print("The number that appears odd number of times:")
oddnum_brute(l)


def find_two_odd_occurrences(arr):
    xor = 0
    for num in arr:
        xor ^= num

    # Find a rightmost set bit in xor (differs a and b)
    set_bit = xor & -xor

    # Initialize results
    num1 = 0
    num2 = 0

    for num in arr:
        if num & set_bit:
            num1 ^= num
        else:
            num2 ^= num

    return num1, num2

# Example usage
arr = [4, 3, 4, 4, 4, 5, 3, 3, 3, 7]
result = find_two_odd_occurrences(arr)
print("The two odd occurring numbers are:", result)
