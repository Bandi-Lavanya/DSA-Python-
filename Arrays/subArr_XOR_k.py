#Count the number of subarrays with given xor K

def subarraysWithXorK_brute(a, b):
    n = len(a)  # size of the given array.
    cnt = 0

    # Step 1: Generating subarrays:
    for i in range(n):
        for j in range(i, n):

            # step 2: calculate XOR of all elements:
            xorr = 0
            for K in range(i, j + 1):
                xorr = xorr ^ a[K]

            # step 3: check XOR and count:
            if (xorr == k):
                cnt += 1

    return cnt

def subarraysWithXorK_better(a, b):
    n = len(a)  # size of the given array.
    cnt = 0

    # Step 1: Generating subarrays:
    for i in range(n):
        xorr = 0
        for j in range(i, n):

            # step 2: calculate XOR of all elements:
            xorr = xorr ^ a[j]

            # step 3: check XOR and count:
            if (xorr == k):
                cnt += 1

    return cnt

def subarraysWithXorK_optimal(a, b):
    n = len(a)  # size of the given array
    xr = 0
    mpp = {}  # dictionary to store prefix XOR frequencies
    mpp[xr] = 1  # XOR of 0 has one count
    cnt = 0

    for i in range(n):
        # Compute prefix XOR
        xr = xr ^ a[i]

        # Find the required prefix XOR (x = xr ^ b)
        x = xr ^ b

        # Count the number of times this XOR has occurred
        cnt += mpp.get(x, 0)

        # Record the current prefix XOR
        mpp[xr] = mpp.get(xr, 0) + 1

    return cnt

a = [4, 2, 2, 6, 4]
k = 6
ans = subarraysWithXorK_brute(a, k)
print("The number of subarrays with XOR k is:", ans) 
ans1 = subarraysWithXorK_better(a, k)
print("The number of subarrays with XOR k is:", ans1) 
ans2 = subarraysWithXorK_optimal(a, k)
print("The number of subarrays with XOR k is:", ans2) 



