#Find the number that appears odd number of times in a list
'''Enter List elements:4 1 2 1 2
The number that appears odd number of times: 4'''
def oddnum_brute(l):
    d={}
    for i in l:
        d[i]= d.get(i, 0) + 1
    for i in d:
        if d[i] % 2 != 0:
            return i
l=list(map(int,input("Enter List elements:").split()))
print("The number that appears odd number of times:",oddnum_brute(l))


def oddnum_optimal(l):
    result = 0
    for i in l:
        result ^= i  # XOR operation
    return result

print("The number that appears odd number of times:",oddnum_optimal(l))