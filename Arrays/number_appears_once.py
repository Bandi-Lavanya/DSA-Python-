def getSingleElement_bruit(arr):
    # Size of the array:
    n = len(arr)
    # Run a loop for selecting elements:
    for i in range(n):
        num = arr[i]  # selected element
        cnt = 0

        # Find the occurrence using linear search:
        for j in range(n):
            if arr[j] == num:
                cnt += 1

        # If the occurrence is 1, return the number:
        if cnt == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1




def getSingleElement_better1(arr):
    # Size of the array:
    n = len(arr)

    # Find the maximum element:
    maxi = max(arr)

    # Declare hash array of size maxi+1
    # And hash the given array:
    hash = [0] * (maxi + 1)
    for num in arr:
        hash[num] += 1

    # Find the single element and return the answer:
    for num in arr:
        if hash[num] == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1





def getSingleElement_better2(arr):
    # Size of the array:
    n = len(arr)

    # Declare the hashmap.
    # And hash the given array:
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1

    # Find the single element and return the answer:
    for num, count in hashmap.items():
        if count == 1:
            return num

    # This line will never execute
    # if the array contains a single element.
    return -1




def getSingleElement_optimal(arr):
    # XOR all the elements:
    xorr = 0
    for num in arr:
        xorr ^= num
    return xorr



arr = [4, 1, 2, 1, 2]
ans1 = getSingleElement_bruit(arr)
print("The single element is:", ans1)
ans2 = getSingleElement_better1(arr)
print("The single element is:", ans2)
ans3 = getSingleElement_better2(arr)
print("The single element is:", ans3)
ans4 = getSingleElement_optimal(arr)
print("The single element is:", ans4)




