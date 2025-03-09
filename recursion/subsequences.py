def solve(i, s, f):
    if i == len(s):
        print(f, end=" ")
        return
    # Picking
    solve(i + 1, s, f + s[i])
    # Not picking (backtracking)
    solve(i + 1, s, f)

s = "abc"
f = ""
print("All possible subsequences are: ")
solve(0, s, f)
