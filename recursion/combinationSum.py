class Solution:
    # This method finds all combinations of candidates that sum to the target
    def findCombinations(self, ind, arr, target, ans, ds):
        # Base case: If we have reached the end of the array
        if ind == len(arr):
            # If the target is zero, it means we found a valid combination
            if target == 0:
                ans.append(list(ds))  # Append the current combination to the result list
            return  # Return as we have exhausted all elements in the array
        
        # Case 1: Include the current element (arr[ind]) in the combination, if it's <= target
        if arr[ind] <= target:
            ds.append(arr[ind])  # Add the current element to the combination
            # Recurse by including arr[ind] and reducing the target
            self.findCombinations(ind, arr, target - arr[ind], ans, ds)
            ds.pop()  # Backtrack: Remove the last element added to try the next possibility
        
        # Case 2: Exclude the current element (arr[ind]) and move to the next index
        self.findCombinations(ind + 1, arr, target, ans, ds)

    # This method is the main entry point for the problem
    def combinationSum(self, candidates, target):
        ans = []  # This will hold all the valid combinations
        # Start the recursion with index 0, the candidates array, the target, and an empty combination list
        self.findCombinations(0, candidates, target, ans, [])
        return ans  # Return all valid combinations

# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 6, 7]  # Candidates array
    target = 7  # The target sum we need to achieve

    # Create an instance of the Solution class
    sol = Solution()
    
    # Call the combinationSum method to find all combinations that sum up to the target
    result = sol.combinationSum(arr, target)

    print("Combinations are: ")  # Print message
    # Loop through each combination in the result and print it
    for combination in result:
        # Join the numbers in the combination with a space and print them
        print(" ".join(map(str, combination)))
