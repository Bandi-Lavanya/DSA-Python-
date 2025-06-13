#Using permutations function
from itertools import permutations

def nextPermutationBruteForce(nums):
    # Step 1: Generate all unique permutations and sort them
    all_perms = sorted(set(permutations(nums)))

    # Step 2: Find the index of current permutation
    for i in range(len(all_perms)):
        if list(all_perms[i]) == nums:
            # Step 3: Return the next permutation if exists
            if i + 1 < len(all_perms):
                return list(all_perms[i + 1])
            else:
                # If current is the last permutation, return the first (wrap-around)
                return list(all_perms[0])

# Example usage:
nums = [1, 2, 3]
print("Next permutation is:", nextPermutationBruteForce(nums))

#using recursion to find permutations
def permute(nums):
    result = []

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result

def nextPermutationManual(nums):
    all_perms = permute(nums)
    all_perms.sort()  # Sort lexicographically

    for i in range(len(all_perms)):
        if all_perms[i] == nums:
            # Return next permutation if exists
            if i + 1 < len(all_perms):
                return all_perms[i + 1]
            else:
                return all_perms[0]  # Wrap around to the first
    return nums  # In case not found (edge case)

# Example usage:
nums = [1, 2, 3]
print("Current permutation:", nums)
print("Next permutation:", nextPermutationManual(nums))


def nextGreaterPermutation(nums):
    n = len(nums)

    # Step 1: Find the break point (first index from right where nums[i] < nums[i+1])
    ind = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            ind = i
            break

    # Step 2: If no break point, reverse the whole array
    if ind == -1:
        nums.reverse()
        return nums

    # Step 3: Find next greater element to the right of ind and swap
    for i in range(n - 1, ind, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break

    # Step 4: Reverse the sublist to the right of ind
    nums[ind + 1:] = reversed(nums[ind + 1:])
    return nums

# Example usage:
A = [2, 1, 5, 4, 3, 0, 0]
ans = nextGreaterPermutation(A)

print("The next permutation is:", ans)
