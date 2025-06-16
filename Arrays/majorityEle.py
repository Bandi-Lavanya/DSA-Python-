#majority element > n/3
def majorityElement_brute(v):
    n = len(v) # size of the list
    ls = [] # list of answers

    for i in range(n):
        # selected element is v[i]:
        # Checking if v[i] is not already
        # a part of the answer:
        if len(ls) == 0 or ls[0] != v[i]:
            cnt = 0
            for j in range(n):
                # counting the frequency of v[i]
                if v[j] == v[i]:
                    cnt += 1

            # check if frquency is greater than n/3:
            if cnt > (n // 3):
                ls.append(v[i])

        if len(ls) == 2:
            break

    return ls

from collections import Counter

def majorityElement_better(arr):
    # Size of the given array
    n = len(arr)
    nums=[]
    # Count the occurrences of each element using Counter
    counter = Counter(arr)

    # Searching for the majority element
    for num, count in counter.items():
        if count > (n // 3):
            nums.append(num)
    return nums



def majorityElement_optimal(v):
    n = len(v)

    cnt1, cnt2 = 0, 0
    el1, el2 = float('-inf'), float('-inf')

    # Extended Boyer-Moore Voting Algorithm
    for i in range(n):
        if cnt1 == 0 and v[i] != el2:
            cnt1 = 1
            el1 = v[i]
        elif cnt2 == 0 and v[i] != el1:
            cnt2 = 1
            el2 = v[i]
        elif v[i] == el1:
            cnt1 += 1
        elif v[i] == el2:
            cnt2 += 1
        else:
            cnt1 -= 1
            cnt2 -= 1

    # Final count to confirm
    cnt1, cnt2 = 0, 0
    for i in range(n):
        if v[i] == el1:
            cnt1 += 1
        elif v[i] == el2:
            cnt2 += 1

    mini = n // 3 + 1
    result = []
    if cnt1 >= mini:
        result.append(el1)
    if cnt2 >= mini:
        result.append(el2)

    return result

# Test input
arr = [2, 1, 1, 3, 1, 2, 2, 6]
ans1 = majorityElement_brute(arr)
print("The majority elements are:", ans1)
ans2 = majorityElement_better(arr)
print("The majority elements are:", ans2)
ans3 = majorityElement_optimal(arr)
print("The majority elements are:", ans3)
