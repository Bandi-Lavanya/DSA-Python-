def majorityElement_brute(arr):
    # Size of the given array
    n = len(arr)

    for i in range(n):
        # Selected element is arr[i]
        cnt = 0
        for j in range(n):
            # Counting the frequency of arr[i]
            if arr[j] == arr[i]:
                cnt += 1

        # Check if frequency is greater than n/2
        if cnt > (n // 2):
            return arr[i]

    return -1






'''from collections import Counter

def majorityElement(arr):
    # Size of the given array
    n = len(arr)

    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 2):
            return num

    return -1'''

def majority_element_better(arr):
    n = len(arr)
    freq = {}

    # Count the frequency of each element
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Find the majority element
    for key, value in freq.items():
        if value > n // 2:
            return key

    return -1


def majorityElement_optimal(arr):
    # Size of the given array
    n = len(arr)
    cnt = 0  # Count
    el = None  # Element

    # Applying the algorithm
    for i in range(n):
        if cnt == 0:
            cnt = 1
            el = arr[i]
        elif el == arr[i]:
            cnt += 1
        else:
            cnt -= 1

    # Checking if the stored element is the majority element
    cnt1 = 0
    for i in range(n):
        if arr[i] == el:
            cnt1 += 1

    if cnt1 > (n / 2):
        return el
    return -1


# Example usage
arr = [2, 2, 1, 1, 1, 2, 2]
ans1 = majority_element_better(arr)
print("The majority element is:", ans1)
ans2 = majorityElement_optimal(arr)
print("The majority element is:", ans2)
ans3 = majorityElement_brute(arr)
print("The majority element is:", ans3)


