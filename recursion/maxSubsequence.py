class Solution:
    def betterString(self, str1, str2):
        # Create sets to store distinct subsequences
        subseq_set1, subseq_set2 = set(), set()
        
        # Compute distinct subsequences
        self.solve(0, str1, "", subseq_set1)
        self.solve(0, str2, "", subseq_set2)
        
        # Return the better string
        return str1 if len(subseq_set1) >= len(subseq_set2) else str2

    def solve(self, i, s, f, subseq_set):
        if i == len(s):
            subseq_set.add(f)  # Add unique subsequence
            return
        
        # Picking the character
        self.solve(i + 1, s, f + s[i], subseq_set)
        # Not picking the character (backtracking)
        self.solve(i + 1, s, f, subseq_set)

# Example Test Cases
sol = Solution()
print(sol.betterString("gfg", "ggg"))  # Output: "gfg"
print(sol.betterString("a", "b"))      # Output: "a"
