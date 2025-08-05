'''Enter List elements:1 2 3
Subsets: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]'''
def subsets(l):
    n = len(l)
    result = []
    for i in range(1 << n):  # 2^n subsets
        subset = []
        for j in range(n):
            if i & (1 << j):  # Check if jth bit is set
                subset.append(l[j])
        result.append(subset)
    return result
l=list(map(int, input("Enter List elements:").split()))
print("Subsets:", subsets(l))